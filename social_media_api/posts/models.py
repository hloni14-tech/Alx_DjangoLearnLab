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

class LikesModel(models.Model):
    post = models.ForeignKey(Posts, related_name='likes', on_delete=models.CASCADE)
    user = model.ForeignKey('auth.user', on_delete=models.CASCADE)

class Notifications(models.Model):
    recipient = models.ForeignKey('auth.user', related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target = models.ForeignKey(Posts, null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)






