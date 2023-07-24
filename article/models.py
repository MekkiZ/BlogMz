from django.conf import settings
from django.db import models
from django.conf import settings
from PIL import Image


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField(blank=False, null=False)
    date = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='article/%Y/%m/%d')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body_comments = models.TextField(blank=False, null=False)
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
