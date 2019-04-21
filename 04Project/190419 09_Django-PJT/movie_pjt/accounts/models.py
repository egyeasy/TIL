from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')