from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings

# Register your models here.
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "thumbnail",)
    readonly_fields = ("thumbnail_preview",)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def thumbnail(self, obj):
        if obj.seo_image:
            return format_html(
                '<img src="{}" style="height: 200px;" />',
                obj.seo_image.url
            )
        return "-"

    thumbnail.short_description = "Preview"

    def thumbnail_preview(self, obj):
        if obj.seo_image:
            return format_html(
                '<img src="{}" style="max-height: 300px;" />',
                obj.seo_image.url
            )
        return "-"
