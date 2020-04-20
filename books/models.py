from django.db import models

class Book(models.Model):
    col = models.CharField(max_length=10)

