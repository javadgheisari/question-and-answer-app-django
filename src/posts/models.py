from django.db import models
from django.contrib.auth.models import User


# Create your models here =>

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    slug = models.SlugField(max_length=150)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'
