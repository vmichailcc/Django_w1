from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Book, Author

def index(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, "index.html", context)


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        context = {"book": book}
        return render(request, "book.html", context)
    except:
        return HttpResponseNotFound(f"Page {pk} not found")


def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        context = {"author": author}
        return render(request, "author.html", context)
    except:
        return HttpResponseNotFound(f"Page {pk} not found")


def author_books(request, pk):
    try:
        books = Book.objects.all()
        author = Author.objects.get(pk=pk)
        context = {
            "books": books,
            "author": author,
        }
        return render(request, "books_list.html", context)
    except:
        return HttpResponseNotFound(f"Page {id} not found")
