from django.db import models

# Create your models here.
class Account(models.Model):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')
    followers = models.ManyToManyField('self', symmetrical=False)
    