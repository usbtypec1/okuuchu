from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ('User',)


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
