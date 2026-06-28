from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class UserType(models.TextChoices):
        PROPRIETARIO = 'proprietario', 'Proprietário'
        INQUILINO = 'inquilino', 'Inquilino'

    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.INQUILINO,
    )

    whatsapp = models.CharField(max_length=20, blank=True, help_text='Número com DDD, ex: 5511999999999')

    def __str__(self):
        return f'{self.username} ({self.get_user_type_display()})'
