from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(models.Model):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')
    followers = models.ManyToManyField('self', symmetrical=False)

class UserModel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    username = models.CharField(max_length=150, unique=True)


    

