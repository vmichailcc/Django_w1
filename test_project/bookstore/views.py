from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .models import Book, Author
from .forms import AddBook, AddAuthor


class BookView(View):
    def get(self, request):
        books = Book.objects.all().order_by("-id")
        if request.method == "GET" and "search" in request.GET:
            search = request.GET["search"]
            books = books.filter(title__icontains=search)
        context = {
            "books": books,
        }
        return render(request, "index.html", context)

    def post(self, request):
        books = Book.objects.all().order_by("-id")
        context = {
            "books": books,
        }
        return render(request, "index.html", context)


class BookDetailView(DetailView):
    model = Book
    template_name = "book.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author.html"


# class AuthorBooksView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         author = Author.objects.get(pk=self.pk)
#         context = {
#             "books": books,
#             "author": author,
#         }
#         return render(request, "books_list.html", context)

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
            print(form)
            print("Invalid Form")
            print(form.errors)
            return render(request, "add_book.html", {'form': form})
    else:
        form = AddBook()
    return render(request, "add_book.html", {"form": form})


def add_author(request):
    if request.method == "POST":
        form_author = AddAuthor(request.POST)
        if form_author.is_valid():
            form_author.save()
            return redirect("add_book")
        else:
            print(form_author)
            print("Invalid Form")
            print(form_author.errors)
            return render(request, "add_author.html", {'form': form_author})
    else:
        form_author = AddAuthor()
    context = {"form_author": form_author}
    return render(request, "add_author.html", context)
