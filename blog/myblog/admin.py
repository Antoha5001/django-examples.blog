from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status', 'author']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']

# Register your models here.
