from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/'
