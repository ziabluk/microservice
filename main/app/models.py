from django.db import models


class Product(models.Model):
    GROUP_CHOICES = [
        ('SNICKERS', 'snickers'),
        ('SHIRTS', 'shirts'),
        ('TROUSERS', 'trousers'),
    ]
    code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    group = models.CharField(max_length=255, choices=GROUP_CHOICES)

    def __str__(self):
        return self.title


class Storage(models.Model):
    title = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name="storage")

    def __str__(self):
        return self.title
