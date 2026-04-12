from django.contrib import admin
from django.utils.html import format_html
from .models import Homepage, About_Article, About_Vani, Article_bkp, Resume, Skill, Language, Reference, Experience, Showreel, Credits, Credits_Category

# Register your models here.

@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ("main_title", "thumbnail")
    readonly_fields = ("thumbnail_preview",)

    def thumbnail(self, obj):
        if obj.hero_image_mobile:
            return format_html(
                '<img src="{}" style="height: 200px;" />',
                obj.hero_image_mobile.url
            )
        return "-"

    thumbnail.short_description = "Preview"

    def thumbnail_preview(self, obj):
        if obj.hero_image_mobile:
            return format_html(
                '<img src="{}" style="max-height: 300px;" />',
                obj.hero_image_mobile.url
            )
        return "-"
    
    def has_add_permission(self, request):
        return not Homepage.objects.exists()

@admin.register(About_Article)
class About_ArticleAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "thumbnail")
    readonly_fields = ("thumbnail_preview",)

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 200px;" />',
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

@admin.register(Showreel)
class ShowreelAdmin(admin.ModelAdmin):
    list_display = ("main_title", "thumbnail_preview" )
    readonly_fields = ("thumbnail_preview",)
    
    def has_add_permission(self, request):
        return not Showreel.objects.exists()
    
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


@admin.register(Credits_Category)
class Credits_CategoryAdmin(admin.ModelAdmin):
    list_display = ("order", "name",)
    readonly_fields = ("slug",)


@admin.register(Credits)
class CreditsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "director", "date", "role")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Credits_Category.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Article_bkpInline(admin.TabularInline):
    model = Article_bkp
    extra = 0
    fields = ("title", "description", "image", "order")


class About_VaniAdmin(admin.ModelAdmin):
    inlines = [Article_bkpInline]

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
        


