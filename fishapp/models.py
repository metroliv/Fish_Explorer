from django.db import models

# Existing Fish Model
class Fish(models.Model):
    species_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    habitat = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    biology = models.TextField(null=True, blank=True)
    population = models.TextField(null=True, blank=True)
    fishing_rate = models.TextField(null=True, blank=True)
    health_benefits = models.TextField(null=True, blank=True)

    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(upload_to='fish_images/', null=True, blank=True)

    management = models.TextField(null=True, blank=True)
    availability = models.TextField(null=True, blank=True)
    nutrition = models.TextField(null=True, blank=True)
    texture = models.CharField(max_length=255, null=True, blank=True)
    taste = models.CharField(max_length=255, null=True, blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.species_name


# ✅ Fish Pod Model
class FishPod(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='fish_pods/', null=True, blank=True)
    capacity = models.CharField(max_length=100, null=True, blank=True)
    suitable_species = models.ManyToManyField(Fish, blank=True)
    maintenance_tips = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# ✅ Fishing Technique Model
class FishingMethod(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='fishing_methods/', null=True, blank=True)
    recommended_species = models.ManyToManyField(Fish, blank=True)
    tools_required = models.TextField(null=True, blank=True)
    is_traditional = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# ✅ Cooking / Preparation Model
class FishPreparation(models.Model):
    name = models.CharField(max_length=255)
    method = models.TextField()
    image = models.ImageField(upload_to='fish_preparations/', null=True, blank=True)
    ingredients = models.TextField()
    steps = models.TextField()
    suitable_species = models.ManyToManyField(Fish, blank=True)

    def __str__(self):
        return self.name
