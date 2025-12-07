from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey()
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
user = models.OneToOneField(User, on_delete=models.CASCADE)
bio = models.TextField(blank=True)
image = models.ImageField(default='default.jpg', upload_to='profile_pics')


def __str__(self):
return f"{self.user.username} Profile"


def save(self, *args, **kwargs):
super().save(*args, **kwargs)


# Optionally resize images
try:
img = Image.open(self.image.path)
if img.height > 300 or img.width > 300:
output_size = (300, 300)
img.thumbnail(output_size)
img.save(self.image.path)
except Exception:
# when using remote storage or default image, ignore
pass
