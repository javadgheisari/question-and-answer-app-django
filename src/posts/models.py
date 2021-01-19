from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here:

CATEGORY_CHOICES = (
    ("1", "اجتماعی"),
    ("2", "اقتصادی"),
    ("3", "درسی"),
    ("4", "سیاسی"),
    ("5", "فرهنگ و هنر"),
)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='1')
    slug = models.SlugField(max_length=150, allow_unicode=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.created.year, self.created.month,
                                                  self.created.day, self.slug])


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomment')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='rcomment')
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'
