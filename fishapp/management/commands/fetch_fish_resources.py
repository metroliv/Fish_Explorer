import requests
from django.core.management.base import BaseCommand
from fishapp.models import FishPod, FishingMethod, FishPreparation
import time

WIKIPEDIA_API = "https://en.wikipedia.org/api/rest_v1/page/summary/"

def fetch_wikipedia_summary(title):
    try:
        url = WIKIPEDIA_API + title.replace(" ", "_")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "title": data.get("title"),
            "description": data.get("extract"),
            "image": data.get("thumbnail", {}).get("source", None)
        }
    except Exception as e:
        print(f"❌ Failed fetching: {title} — {e}")
        return None

class Command(BaseCommand):
    help = "Fetch general information for fish pods, fishing methods, and fish preparations."

    def handle(self, *args, **kwargs):
        # =============================
        # 📦 Fish Pods
        # =============================
        pod_titles = [
            "Aquarium", "Fish pond", "Aquaponics", "Aquaculture", "Fish tank", "Recirculating aquaculture system"
        ]

        for title in pod_titles:
            info = fetch_wikipedia_summary(title)
            if info:
                FishPod.objects.get_or_create(
                    name=info['title'],
                    defaults={
                        "description": info['description'],
                        "image": info['image'],
                        "capacity": "Varies",
                        "maintenance_tips": "Ensure water filtration, pH balance, and periodic cleaning."
                    }
                )
                print(f"✅ Saved FishPod: {info['title']}")
            time.sleep(0.3)

        # =============================
        # 🎣 Fishing Methods
        # =============================
        fishing_titles = [
            "Angling", "Trawling", "Gillnetting", "Spearfishing", "Longline fishing", "Fly fishing", "Ice fishing"
        ]

        for title in fishing_titles:
            info = fetch_wikipedia_summary(title)
            if info:
                FishingMethod.objects.get_or_create(
                    name=info['title'],
                    defaults={
                        "description": info['description'],
                        "image": info['image'],
                        "tools_required": "Varies by method (e.g., hooks, nets, spears)",
                        "is_traditional": title.lower() in ["angling", "spearfishing", "fly fishing"]
                    }
                )
                print(f"✅ Saved FishingMethod: {info['title']}")
            time.sleep(0.3)

        # =============================
        # 🍽️ Fish Preparations
        # =============================
        preparation_titles = [
            "Fish curry", "Grilled fish", "Fried fish", "Sushi", "Ceviche", "Fish and chips", "Smoked fish"
        ]

        for title in preparation_titles:
            info = fetch_wikipedia_summary(title)
            if info:
                FishPreparation.objects.get_or_create(
                    name=info['title'],
                    defaults={
                        "method": info['description'],
                        "image": info['image'],
                        "ingredients": "Fish, spices, herbs, oil, lemon, salt (varies)",
                        "steps": f"See Wikipedia article for steps: https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                    }
                )
                print(f"✅ Saved FishPreparation: {info['title']}")
            time.sleep(0.3)

        self.stdout.write(self.style.SUCCESS("🎉 Finished importing Fish Resources from Wikipedia"))
