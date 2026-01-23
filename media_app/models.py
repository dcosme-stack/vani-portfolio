from django.db import models
from core.models import FileCleanupModel
from autoslug import AutoSlugField

class Category(models.Model):
    CONTENT_TYPES = [
        ("photo", "Photo"),
        ("video", "Video"),
    ]

    name = models.CharField(max_length=50)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    slug = AutoSlugField(populate_from="name")

    class Meta:
        unique_together = ("name", "content_type")
        verbose_name_plural = "Categories"
        ordering = ["content_type","name"]
        constraints = [
            models.UniqueConstraint(
                fields=["slug", "content_type"],
                name="unique_category_slug_per_content_type"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.content_type})"


class Photo(FileCleanupModel):
    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"content_type": "photo"},
    )
    image = models.ImageField(upload_to="photos/gallery")
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"content_type": "video"},
    )
    youtube_id = models.CharField(
        max_length=11,
        help_text="Paste only the YouTube video ID (11 characters)"
    )
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title