from django.db import models
from django.contrib.auth.models import AbstractUser


class UserCus(AbstractUser):
    groups = (
        ('regular', 'regular'),
        ('moderator', 'moderator'),
        ('publisher', 'publisher'),

    )

    username = models.CharField(max_length=20,unique=True, blank=False, null=False)
    mail = models.CharField(max_length=40, null=False)
    birthday = models.DateField()
    group = models.CharField(max_length=30, choices=groups, blank=False, null=False, default='regular')
    password = models.CharField(max_length=20, null=False, blank=False)
    date_joined = models.DateField(auto_now_add=True, blank=True)
    job = models.CharField(max_length=30)
