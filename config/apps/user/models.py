from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Создает модель данных о пользователе"""
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return self.username