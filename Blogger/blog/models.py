from turtle import mode
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class BlogPost(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}" 