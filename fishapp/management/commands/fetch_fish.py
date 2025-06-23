import requests
import time
from django.core.management.base import BaseCommand
from fishapp.models import Fish

class Command(BaseCommand):
    help = 'Fetch 10,000+ fish data entries from Wikipedia and store in the database'

    def handle(self, *args, **kwargs):
        search_url = "https://en.wikipedia.org/w/api.php"
        summary_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"

        total_fetched = 0
        batch_size = 500
        max_batches = 20  # 500 * 20 = 10,000
        offset = 0

        for batch in range(max_batches):
            params = {
                "action": "query",
                "list": "search",
                "srsearch": "fish",
                "format": "json",
                "srlimit": batch_size,
                "sroffset": offset,
            }

            try:
                response = requests.get(search_url, params=params, timeout=15)
                response.raise_for_status()
                results = response.json().get("query", {}).get("search", [])
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Batch {batch+1} search failed: {e}"))
                break

            for result in results:
                title = result.get("title")
                if not title:
                    continue

                try:
                    page_summary_url = summary_url + title.replace(" ", "_")
                    res = requests.get(page_summary_url, timeout=10)
                    res.raise_for_status()
                    data = res.json()

                    Fish.objects.get_or_create(
                        species_name=data.get("title", title),
                        defaults={
                            "scientific_name": "",
                            "category": "Wikipedia Entry",
                            "habitat": "",
                            "location": "",
                            "biology": data.get("extract", ""),
                            "population": "",
                            "fishing_rate": "",
                            "health_benefits": "",
                            "image_url": data.get("thumbnail", {}).get("source"),
                            "management": "",
                            "availability": "",
                            "nutrition": "",
                            "texture": "",
                            "taste": "",
                        }
                    )
                    total_fetched += 1
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"⚠️ Skipped {title}: {e}"))
                time.sleep(0.2)  # Respect Wikipedia’s servers

            offset += batch_size
            self.stdout.write(self.style.SUCCESS(f"✅ Batch {batch+1} done. Total so far: {total_fetched}"))

        self.stdout.write(self.style.SUCCESS(f"🎉 Finished. Total fish-related articles imported: {total_fetched}"))
