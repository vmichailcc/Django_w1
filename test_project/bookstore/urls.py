"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import BookView, BookDetailView, AuthorDetailView, author_books, add_book, add_author

urlpatterns = [
    path('', BookView.as_view(), name="index"),
    path('book/<int:pk>', BookDetailView.as_view(), name="book"),
    path('author/<int:pk>', AuthorDetailView.as_view(), name="author"),
    path('books/<int:pk>', author_books, name="books_list"),
    path('add_book/', add_book, name="add_book"),
    path('add_author/', add_author, name="add_author"),
]
