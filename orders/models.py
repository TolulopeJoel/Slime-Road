from django.db import models

from shop.models import Product


class Order(models.Model):
    product = models.ForeignKey(
        Product,
        null=True,
        related_name='orders',
        on_delete=models.SET_NULL
    )
    email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.email
