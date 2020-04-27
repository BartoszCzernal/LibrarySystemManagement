from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'
