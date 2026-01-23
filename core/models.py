from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver



class FileCleanupModel(models.Model):
    """
    Abstract base model that deletes files when:
    - the object is deleted
    - a File/ImageField is replaced
    """

    class Meta:
        abstract = True

@receiver(post_delete)
def delete_files_on_delete(sender, instance, **kwargs):
    if not issubclass(sender, FileCleanupModel):
        return

    for field in sender._meta.fields:
        if isinstance(field, (models.FileField, models.ImageField)):
            file = getattr(instance, field.name)
            if file:
                file.delete(save=False)

@receiver(pre_save)
def delete_old_files_on_change(sender, instance, **kwargs):
    if not issubclass(sender, FileCleanupModel):
        return

    if not instance.pk:
        return

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    for field in sender._meta.fields:
        if isinstance(field, (models.FileField, models.ImageField)):
            old_file = getattr(old_instance, field.name)
            new_file = getattr(instance, field.name)

            if old_file and old_file != new_file:
                old_file.delete(save=False)


class SiteSettings(FileCleanupModel):
    class Meta:
        verbose_name = "Global Settings"
        verbose_name_plural = "Global Settings"
    site_name = models.CharField(max_length=100)
    actress_name = models.CharField(max_length=100, blank=True)
    facebook_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    email = models.EmailField()
    footer = models.CharField(max_length=100)
    site_url = models.URLField(blank=True)
    seo_image = models.ImageField(
        upload_to="photos/seo",
        blank=True,
        null=True
        )