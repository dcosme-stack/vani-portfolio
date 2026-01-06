from django.db import models
from core.models import FileCleanupModel

# Create your models here.
class Category(models.TextChoices):
    COMEDY = "comedy", "Comedy"
    HORROR = "horror", "Horror"
    DRAMA = "drama", "Drama"
    OTHERS = "others", "Others"

class Photo(FileCleanupModel):
    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHERS,
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
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHERS,
    )
    youtube_id = models.CharField(
        max_length=11,
        help_text="Paste only the YouTube video ID (11 characters)"
    )
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title