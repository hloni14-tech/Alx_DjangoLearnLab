from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey()
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    