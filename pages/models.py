from django.db import models
from core.models import FileCleanupModel
from django_ckeditor_5.fields import CKEditor5Field
from autoslug import AutoSlugField

# Create your models here.
class Homepage(FileCleanupModel):
    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"
    main_title = models.CharField(max_length=100)
    short_description = CKEditor5Field(
        "Short Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.",
        blank=True)
    hero_image_mobile = models.ImageField(
        upload_to="photos/homepage",
        blank=True,
        help_text="768px portrait for mobile")
    hero_image_laptop = models.ImageField(
        upload_to="photos/homepage",
        blank=True,
        help_text="1280px landscape for laptop")
    hero_image_desktop = models.ImageField(
        upload_to="photos/homepage",
        blank=True,
        help_text="1920px wide landscape for desktop")
    about_me_title = models.CharField(max_length=100, blank=True)
    detailed_description = CKEditor5Field(
        "Detailed Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.",
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_title
    
class About_Article(FileCleanupModel):
    class Meta:
        verbose_name = "Homepage - Article"
        verbose_name_plural = "Homepage - Articles"
        ordering = ["order"]

    about_vani = models.ForeignKey(
        Homepage,
        on_delete=models.CASCADE,
        related_name="articles"
    )
    title = models.CharField(max_length=100)
    description = CKEditor5Field(
        "Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.")
    image = models.ImageField(upload_to="photos/about")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Showreel(FileCleanupModel):
    class Meta:
        verbose_name = "Showreel"
        verbose_name_plural = "Showreel"
    main_title = models.CharField(max_length=100, blank=True)
    description = CKEditor5Field(
        "Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.",
        blank=True)
    video_title = models.CharField(max_length=100, blank=True)
    youtube_id = models.CharField(
        max_length=11,
        help_text="Paste only the YouTube video ID (11 characters)",
        blank=True)
    video = models.FileField(
        upload_to="videos/showreel",
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_title
    
class About_Vani(FileCleanupModel):
    class Meta:
        verbose_name = "About bkp"
        verbose_name_plural = "About bkp"
    main_title = models.CharField(max_length=100)
    main_description = CKEditor5Field(
        "Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.")
    main_picture = models.ImageField(
        upload_to="photos/about",
        blank=True,
        null=True
        )

    def __str__(self):
        return self.main_title

class Article_bkp(FileCleanupModel):
    class Meta:
        verbose_name = "Article_bkp"
        verbose_name_plural = "Articles_bkp"
        ordering = ["order"]

    about_vani = models.ForeignKey(
        About_Vani,
        on_delete=models.CASCADE,
        related_name="articles_bkp"
    )
    title = models.CharField(max_length=100)
    description = CKEditor5Field(
        "Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.")
    image = models.ImageField(upload_to="photos/about")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Credits_Category(models.Model):
    class Meta:
        verbose_name = "Credits Category"
        verbose_name_plural = "Credits Category"
        ordering = ["order"]
    name = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return self.name

class Credits(models.Model):
    class Meta:
        verbose_name = "Credit"
        verbose_name_plural = "Credits"
        ordering = ["category"]
    title = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(
        Credits_Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    director = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)

class Resume(FileCleanupModel):
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"
    main_title = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    main_info = CKEditor5Field(
        "Main_Info",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.")
    profile = CKEditor5Field(
        "Profile",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.")
    resume_pic = models.ImageField(upload_to="photos/resume")
    resume_file = models.FileField(
        upload_to='files/resume',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_title
    
class Skill(models.Model):
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="skills"
    )
    skill_name = models.CharField(max_length=100)
    skill_level = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.skill_name
    
class Language(models.Model):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="languages"
    )
    language_name = models.CharField(max_length=100)
    language_level = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.language_name
    
class Reference(models.Model):
    class Meta:
        verbose_name = "Reference"
        verbose_name_plural = "References"
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="references"
    )
    ref_fullname = models.CharField(max_length=100)
    ref_phone = models.CharField(max_length=100)

    def __str__(self):
        return self.ref_fullname
    
class Experience(models.Model):
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="experiences"
    )
    title = models.CharField(max_length=100)
    description = CKEditor5Field(
        "Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title