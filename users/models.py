from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from . manager import CustomUserManager


class customuser(AbstractUser):
    """A custom user"""
    username = None
    email = models.EmailField(_("email_address"), unique=True)
    first_name = models.CharField()
    last_name = models.CharField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name",]
    objects = CustomUserManager()

    def __str__(self):
        return self.email