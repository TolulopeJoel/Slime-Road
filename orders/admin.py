from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'product', 'created_at', 'paid']

admin.site.register(Order, OrderAdmin)
