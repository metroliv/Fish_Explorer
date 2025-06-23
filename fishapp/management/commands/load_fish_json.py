import json
import os
from django.core.management.base import BaseCommand
from fishapp.models import Fish

class Command(BaseCommand):
    help = 'Load fish data from a local JSON file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join('fishdata', 'fish_species.json')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"❌ JSON file not found at: {file_path}"))
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Failed to load JSON: {e}"))
                return

        count = 0
        for item in data:
            try:
                Fish.objects.get_or_create(
                    species_name=item.get("Species Name", "Unknown"),
                    defaults={
                        "scientific_name": item.get("Scientific Name", ""),
                        "category": item.get("Species Illustration Photo", {}).get("alt", ""),
                        "habitat": item.get("Habitat", ""),
                        "location": item.get("Location", ""),
                        "biology": item.get("Biology", ""),
                        "population": item.get("Population", ""),
                        "fishing_rate": item.get("Fishing Rate", ""),
                        "health_benefits": item.get("Health Benefits", ""),
                        "image_url": item.get("Species Illustration Photo", {}).get("src", ""),
                        "management": item.get("Management", ""),
                        "availability": item.get("Availability", ""),
                        "nutrition": item.get("Nutrition", ""),
                        "texture": item.get("Texture", ""),
                        "taste": item.get("Taste", ""),
                    }
                )
                count += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"⚠️ Skipped: {e}"))

        self.stdout.write(self.style.SUCCESS(f"✅ Loaded {count} fish from JSON."))
