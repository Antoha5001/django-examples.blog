from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_CHOISED = (('drafted', 'Drafted'), ('published', 'Published'))

class Blog(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-publish']


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    status = models.CharField(max_length=10, choices=STATUS_CHOISED, default='draft')

    def __str__(self):
        return f'{self.title}'



# Create your models here.
