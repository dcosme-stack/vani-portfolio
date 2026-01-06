from django.contrib import admin
from .models import SiteSettings

# Register your models here.
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "email", "footer")

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
