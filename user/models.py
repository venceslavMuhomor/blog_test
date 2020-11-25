from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Account(AbstractUser):
    GENDER_CHOICES = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
        ('Н', 'Небинарный')
    )

    birth_date = models.DateField(
        'Дата рождения',
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
    )
    avatar_image = models.ImageField(upload_to='media/profile', max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    def __str__(self):
         return self.get_username()

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
