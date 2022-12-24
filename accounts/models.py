from django.db import models
from django.contrib.auth.models import AbstractUser

class Creator(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='creator/%Y/%m/%d')