from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def index(request):
    books = Book.objects.all()
    if request.method == "GET" and "search" in request.GET:
        search = request.GET["search"]
        books = books.filter(title__icontains=search)
    context = {
        "books": books,
    }
    return render(request, "index.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, "book.html", context)


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
