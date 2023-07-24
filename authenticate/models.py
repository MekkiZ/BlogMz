from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class UserCus(AbstractUser):
    groups = (
        ('regular', 'regular'),
        ('moderator', 'moderator'),
        ('publisher', 'publisher'),

    )

    username = models.CharField(max_length=100,unique=True, blank=False, null=False)
    mail = models.CharField(max_length=100, null=False)
    group = models.CharField(max_length=100, choices=groups, blank=True, null=False, default='regular')
    password = models.CharField(max_length=100, null=False, blank=False)
    date_joined = models.DateField(auto_now_add=True, blank=True)
    job = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='Profile/%Y/%m/%d')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 180 or img.width > 180:
            output_size = (180, 180)
            img.thumbnail(output_size)
            img.save(self.image.path)
