from django.urls import path, include
from .views import BookView, AuthorDetailView, BookInfoView, BookAuthor, AddBookForm, AddAuthorForm

urlpatterns = [
    path('', BookView.as_view(), name="index"),
    path('book/<int:pk>', BookInfoView.as_view(), name="book"),
    path('author/<int:pk>', AuthorDetailView.as_view(), name="author"),
    path('books/<int:pk>', BookAuthor.as_view(), name="books_list"),
    path('add_book/', AddBookForm.as_view(), name="add_book"),
    path('add_author/', AddAuthorForm.as_view(), name="add_author"),
]

