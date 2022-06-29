from django.urls import path, include
from .views import BookView, AuthorDetailView, BookInfoView, author_books, add_book, add_author

urlpatterns = [
    path('', BookView.as_view(), name="index"),
    path('book/<int:pk>', BookInfoView.as_view(), name="book"),
    path('author/<int:pk>', AuthorDetailView.as_view(), name="author"),
    path('books/<int:pk>', author_books, name="books_list"),
    path('add_book/', add_book, name="add_book"),
    path('add_author/', add_author, name="add_author"),
]

