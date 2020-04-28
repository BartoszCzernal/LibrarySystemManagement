from django.urls import path
from . import views
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail')
]