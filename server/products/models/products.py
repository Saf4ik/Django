from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=255, unique=True
    )
    description = models.TextField(
        blank=True, null=True,
    )
    image = models.ImageField(
        upload_to='products',
        blank=True, null=True,
    )
    category = models.ForeignKey(
        'products.Category',
        related_name='products',
        on_delete=models.CASCADE
    )
    cost = models.DecimalField(
        max_digits=12, decimal_places=2, 
        default=0
    )
    modifield = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
