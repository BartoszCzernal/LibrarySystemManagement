from django.shortcuts import render
from .models import Book, Author
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookForm


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/'


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    context_object_name = 'author'


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = '/'
