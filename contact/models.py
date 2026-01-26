from django.db import models

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"
