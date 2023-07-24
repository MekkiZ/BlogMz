from django.db import models
from django.conf import settings


class UserLogin(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30, blank=False, null=False)
    profession = models.CharField(max_length=40)
    hobbies = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'
