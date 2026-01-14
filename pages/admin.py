from django.contrib import admin
from django.utils.html import format_html
from .models import Homepage, About_Vani, Article, Resume, Skill, Language, Reference, Experience

# Register your models here.

@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ("main_title", "thumbnail")
    readonly_fields = ("thumbnail_preview",)

    def thumbnail(self, obj):
        if obj.hero_image:
            return format_html(
                '<img src="{}" style="height: 200px;" />',
                obj.hero_image.url
            )
        return "-"

    thumbnail.short_description = "Preview"

    def thumbnail_preview(self, obj):
        if obj.hero_image:
            return format_html(
                '<img src="{}" style="max-height: 300px;" />',
                obj.hero_image.url
            )
        return "-"
    
    def has_add_permission(self, request):
        return not Homepage.objects.exists()


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0
    fields = ("title", "description", "image", "order")

@admin.register(About_Vani)
class About_VaniAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

    list_display = ("main_title", "main_description","thumbnail")
    readonly_fields = ("thumbnail_preview",)

    def thumbnail(self, obj):
        if obj.main_picture:
            return format_html(
                '<img src="{}" style="height: 200px;" />',
                obj.main_picture.url
            )
        return "-"

    thumbnail.short_description = "Preview"

    def thumbnail_preview(self, obj):
        if obj.main_picture:
            return format_html(
                '<img src="{}" style="max-height: 300px;" />',
                obj.main_picture.url
            )
        return "-"
    
    def has_add_permission(self, request):
        return not About_Vani.objects.exists()
    
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    #fields = ("Skill Name", "Skill Level")

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0

class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 0
    #fields = ("ref_fullname", "ref_phone")

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0
    fields = ("order","title", "description")

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
        LanguageInline,
        ReferenceInline,
        ExperienceInline,
        ]
    
    list_display = ("main_title",)
    readonly_fields = ("thumbnail_preview",)

    def thumbnail_preview(self, obj):
        if obj.resume_pic:
            return format_html(
                '<img src="{}" style="max-height: 300px;" />',
                obj.resume_pic.url
            )
        return "-"
    
    def has_add_permission(self, request):
        return not Resume.objects.exists()
        
    
