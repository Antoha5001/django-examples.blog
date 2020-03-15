from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOISED = (('drafted', 'Drafted'), ('published', 'Published'))

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='published')

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
	objects = models.Manager()
	published = PublishedManager()

	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('blog:detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])



# Create your models here.
