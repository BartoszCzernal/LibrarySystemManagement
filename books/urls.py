from django.urls import path
from django.conf.urls import url
from django import views as django_views
from .views import BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('new/', BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]