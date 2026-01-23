from django.db import models
from core.models import FileCleanupModel
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Homepage(FileCleanupModel):
    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"
    main_title = models.CharField(max_length=100)
    description = CKEditor5Field(
        "Description",
        config_name="simple_text",
        help_text="You can use bold, italics, lists and links.")
    hero_image = models.ImageField(upload_to="photos/homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_title
    
class About_Vani(FileCleanupModel):
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
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
    
class Article(FileCleanupModel):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["order"]

    about_vani = models.ForeignKey(
        About_Vani,
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