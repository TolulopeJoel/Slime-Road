from django.contrib import admin

from .models import Creator


class CreatorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff']

admin.site.register(Creator, CreatorAdmin)
