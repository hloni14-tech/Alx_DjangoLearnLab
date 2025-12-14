from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    




