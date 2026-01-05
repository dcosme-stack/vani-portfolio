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
    list_display = ("title", "category", "thumbnail_preview", "is_featured", "created_at")
    list_filter = ("is_featured","category",)
    search_fields = ("title",)
    readonly_fields = ("thumbnail_preview",)

    def thumbnail_preview(self, obj):
        if not obj.youtube_id:
            return "No video"

        thumbnail_url = f"https://img.youtube.com/vi/{obj.youtube_id}/hqdefault.jpg"
        youtube_url = f"https://www.youtube.com/watch?v={obj.youtube_id}"

        return format_html(
            """
            <a href="{}" target="_blank">
                <img src="{}" style="max-width:300px; max-height: 200px; border-radius:6px;" />
            </a>
            """,
            youtube_url,
            thumbnail_url,
            youtube_url
        )

    thumbnail_preview.short_description = "Preview"