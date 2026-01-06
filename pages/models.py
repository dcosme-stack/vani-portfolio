from django.db import models
from core.models import FileCleanupModel

# Create your models here.
class Homepage(FileCleanupModel):
    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"
    main_title = models.CharField(max_length=100)
    description = models.TextField()
    hero_image = models.ImageField(upload_to="photos/homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_title
    
class About_Vani(models.Model):
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
    main_title = models.CharField(max_length=100)

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
    description = models.TextField()
    image = models.ImageField(upload_to="photos/about")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Resume(FileCleanupModel):
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"
    main_title = models.CharField(max_length=100)
    main_info = models.TextField()
    profile = models.TextField()
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
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title