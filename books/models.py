from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    isbn = ISBNField(null=True)
    title = models.CharField(max_length=100, null=True)
    

