from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=255, unique=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.name
