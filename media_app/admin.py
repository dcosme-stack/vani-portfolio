from django.contrib import admin
from django.utils.html import format_html
from .models import Photo, Video

# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail", "category", "is_featured", "created_at")
    list_filter = ("is_featured","category",)
    search_fields = ("title",)
    readonly_fields = ("thumbnail_preview",)

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 50px;" />',
                obj.image.url
            )
        return "-"

    thumbnail.short_description = "Preview"

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 300px;" />',
                obj.image.url
            )
        return "-"


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "created_at")
    list_filter = ("is_featured","category",)
    search_fields = ("title",)