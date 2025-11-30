from django.db import models

class Author(models.Model):
  author = model.CharField(max_length=200)

class Book(models.Model):
  title = model.CharField(max_length=190) 
  name = model.ForeignKey(Author, max_length=900)
  publication_year = model.DateField()
  
# Create your models here.



