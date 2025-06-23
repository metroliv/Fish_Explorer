import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from fishapp.models import Fish

class Command(BaseCommand):
    help = 'Import fish data from a local CSV file into the database'

    def handle(self, *args, **kwargs):
        # ✅ Path to your CSV file inside 'fishdata' directory at project root
        file_path = os.path.join(settings.BASE_DIR, 'fishdata', 'fish_species1.csv')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"❌ File not found: {file_path}"))
            return

        count = 0
        skipped = 0

        try:
            with open(file_path, mode='r', encoding='utf-8', errors='ignore') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    species_name = row.get("species_name") or row.get("Species Name") or ""
                    species_name = species_name.strip()

                    if not species_name:
                        skipped += 1
                        continue  # Skip rows without a species name

                    try:
                        Fish.objects.get_or_create(
                            species_name=species_name,
                            defaults={
                                "scientific_name": row.get("scientific_name", row.get("Scientific Name", "")).strip(),
                                "category": row.get("category", "").strip(),
                                "habitat": row.get("habitat", row.get("Habitat", "")).strip(),
                                "location": row.get("location", row.get("Location", "")).strip(),
                                "biology": row.get("biology", row.get("Biology", "")).strip(),
                                "population": row.get("population", row.get("Population", "")).strip(),
                                "fishing_rate": row.get("fishing_rate", row.get("Fishing Rate", "")).strip(),
                                "image_url": row.get("image_url", row.get("Image", "")).strip(),
                                "health_benefits": row.get("health_benefits", row.get("Health Benefits", "")).strip(),
                                "management": row.get("management", "").strip(),
                                "availability": row.get("availability", "").strip(),
                                "nutrition": row.get("nutrition", "").strip(),
                                "texture": row.get("texture", "").strip(),
                                "taste": row.get("taste", "").strip(),
                            }
                        )
                        count += 1
                    except Exception as e:
                        skipped += 1
                        self.stdout.write(self.style.WARNING(
                            f"⚠️ Skipped row ({species_name}) due to error: {e}"
                        ))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Failed to read CSV: {e}"))
            return

        # ✅ Final output
        self.stdout.write(self.style.SUCCESS(f"✅ Successfully imported {count} fish entries."))
        if skipped:
            self.stdout.write(self.style.WARNING(f"⚠️ Skipped {skipped} rows (missing data or errors)."))
