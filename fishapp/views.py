from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Fish, FishPod, FishingMethod, FishPreparation

# 🐟 List all fish with pagination
def fish_list(request):
    all_fish = Fish.objects.exclude(image_url__isnull=True).exclude(image_url__exact='')
    paginator = Paginator(all_fish, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "fishapp/fish_list.html", {"fish": page_obj})


# 📄 View a single fish detail
def fish_detail(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    return render(request, "fishapp/fish_detail.html", {"fish": fish})


# 📘 General fish care guide
# views.py
# from .models import FishPod, FishPreparation

def fish_keeping_guide(request):
    pods = FishPod.objects.exclude(image__isnull=True).exclude(image__exact='')
    preparations = FishPreparation.objects.exclude(image__isnull=True).exclude(image__exact='')
    return render(request, "fishapp/guide.html", {
        "pods": pods,
        "preparations": preparations
    })


# 🧱 View all fish pods
def fish_pods(request):
    pods = FishPod.objects.exclude(image__isnull=True).exclude(image__exact='')
    return render(request, "fishapp/fish_pods.html", {"pods": pods})


# 🎣 View all fishing methods
def fishing_methods(request):
    methods = FishingMethod.objects.exclude(image__isnull=True).exclude(image__exact='')
    return render(request, "fishapp/fishing_methods.html", {"methods": methods})


# 🍽️ View all fish cooking/preparation methods
def fish_preparations(request):
    preparations = FishPreparation.objects.exclude(image__isnull=True).exclude(image__exact='')
    return render(request, "fishapp/fish_preparations.html", {"preparations": preparations})
