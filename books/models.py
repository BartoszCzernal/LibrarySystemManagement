from django.db import models
from isbn_field import ISBNField
from datetime import date


class Book(models.Model):
    isbn = ISBNField(null=True)
    title = models.CharField(max_length=100, null=True)
    date_of_release = models.DateField(null=True)
    # on_loan_to : ForeignKey Client
    # owned_by : ForeignKey Library
    # categories : ManyToMany Category
    # authors : ManyToMany Authors
    
    

