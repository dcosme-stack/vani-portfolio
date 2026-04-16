from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("firstname", "lastname", "email", "message")
    readonly_fields = ("firstname", "lastname", "email", "subject", "message", "created_at")

    def has_add_permission(self, request):
        return False  # admin cannot create messages manually