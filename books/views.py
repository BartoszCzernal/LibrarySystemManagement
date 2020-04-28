from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'