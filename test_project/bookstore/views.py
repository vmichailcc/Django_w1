from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Book, Author
from .forms import AddBook, AddAuthor


def index(request):
    books = Book.objects.all().order_by("-id")
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
    author = get_object_or_404(Author, pk=pk)
    context = {"author": author}
    return render(request, "author.html", context)


def author_books(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = get_list_or_404(Book)
    context = {
        "books": books,
        "author": author,
    }
    return render(request, "books_list.html", context)


def add_book(request):
    if request.method == "POST":
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddBook()
    context = {"form": form}
    return render(request, "add_book.html", context)


def add_author(request):
    if request.method == "POST":
        form_author = AddAuthor(request.POST)
        if form_author.is_valid():
            form_author.save()
            return redirect("add_book")
    else:
        form_author = AddAuthor()
    context = {"form_author": form_author}
    return render(request, "add_author.html", context)
