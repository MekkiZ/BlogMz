from django.db import models
from django.conf import settings


class Post(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pseudo = models.CharField(max_length=10, blank=False, null=False)
    title = models.CharField(max_length=300)
    body = models.TextField(blank=False, null=False)
    date = models.DateField()

    def __str__(self):
        return f'{self.title}'


class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body_comments = models.TextField(blank=False, null=False)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
