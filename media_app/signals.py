import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Photo


@receiver(post_delete, sender=Photo)
def delete_photo_file_on_delete(sender, instance, **kwargs):
    """
    Deletes image file from filesystem
    when corresponding Photo object is deleted.
    """
    if instance.image and instance.image.path:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(pre_save, sender=Photo)
def delete_old_photo_on_change(sender, instance, **kwargs):
    """
    Deletes old image file when updating Photo with a new image.
    """
    if not instance.pk:
        return

    try:
        old_image = Photo.objects.get(pk=instance.pk).image
    except Photo.DoesNotExist:
        return

    new_image = instance.image

    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)