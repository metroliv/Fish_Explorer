from django.contrib import admin
from .models import Fish, FishPod, FishingMethod, FishPreparation
from django.utils.html import format_html


@admin.register(Fish)
class FishAdmin(admin.ModelAdmin):
    list_display = ("species_name", "scientific_name", "category", "last_updated", "preview_image")
    search_fields = ("species_name", "scientific_name", "category")
    list_filter = ("category",)
    readonly_fields = ("last_updated",)

    def preview_image(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" width="80" height="50" style="object-fit:cover;">', obj.image_file.url)
        elif obj.image_url:
            return format_html('<img src="{}" width="80" height="50" style="object-fit:cover;">', obj.image_url)
        return "No Image"
    preview_image.short_description = "Image"


@admin.register(FishPod)
class FishPodAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "preview_image")
    search_fields = ("name", "description")
    filter_horizontal = ("suitable_species",)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="50" style="object-fit:cover;">', obj.image.url)
        return "No Image"
    preview_image.short_description = "Image"


@admin.register(FishingMethod)
class FishingMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "is_traditional", "preview_image")
    search_fields = ("name", "description", "tools_required")
    list_filter = ("is_traditional",)
    filter_horizontal = ("recommended_species",)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="50" style="object-fit:cover;">', obj.image.url)
        return "No Image"
    preview_image.short_description = "Image"


@admin.register(FishPreparation)
class FishPreparationAdmin(admin.ModelAdmin):
    list_display = ("name", "preview_image")
    search_fields = ("name", "method", "ingredients")
    filter_horizontal = ("suitable_species",)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="50" style="object-fit:cover;">', obj.image.url)
        return "No Image"
    preview_image.short_description = "Image"
