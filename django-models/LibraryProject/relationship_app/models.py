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



