from django.db import models
from isbn_field import ISBNField


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)


class Category(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    isbn = ISBNField(null=True)
    title = models.CharField(max_length=100, null=True)
    date_of_release = models.DateField(null=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    # on_loan_to : ForeignKey Client
    # owned_by : ForeignKey Library


    
    

