# main/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'  # Используем email для входа
    REQUIRED_FIELDS = ['username']  # username всё ещё требуется (но можно убрать, если нужно)

    def __str__(self):
        return self.email


from django.db import models

# Create your models here.
