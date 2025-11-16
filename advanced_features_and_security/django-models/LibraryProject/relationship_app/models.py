from django.db import models
    
class Author(models.Model):
    name = models.CharField(max_length = 500)  

from django.db import models

class Category(models.Model):     
    author = models.CharField(max_length=200)

class Product(models.Model):
   title = models.CharField(max_length=500)
   category = models.ForeignKey(Category,on_delete=models.CASADE,related_name='category')
   
from django.db import models

class Name(models.Model):
    name = models.CharField(max_length = 200)
    return self.name
    
class Book(models.Model):    
    books  = models.CharField(max_length = 100)
    books = models.ManyToManyField(Name,related_name = 'name')
    
    class Meta, permissions:
    "can_add_book", "can_change_book", "can_delete_book"

from django.db import models

class Librarian(models.Model):
    name = models.CharField(max_length = 200)

class library(models.Model):
    library = models.OneToOneField(Librarian,on_delete=models.CASCADE) 

from django.contrib.auth.models import User

user = User.objects.create.user()


user = User.objects.get()

class UserProfile(models.Model): 
    "Admin", "Member"


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('User', 'User')
    ])



from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Birth(models.Model):
    date_of_birth = models.DateField()










