from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name