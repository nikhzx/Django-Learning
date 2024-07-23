from django.contrib import admin
from .models import User, BlogPost, Comment
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password', 'date_joined']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'status']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']