from django.db import models

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=200)

class Author(models.Model):
    author = models.ForeignKey()

class Content(models.Model):
    content = models.TextField()

class Date(models.Model):
    published_date = models.DateField(auto_now_add=True)