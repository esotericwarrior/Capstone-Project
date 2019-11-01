from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
