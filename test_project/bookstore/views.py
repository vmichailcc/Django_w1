from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .models import Book, Author, BookReview
from .forms import AddBook, AddAuthor, AddBookReview
from django.views.generic import FormView


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


class BookInfoView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        review = get_list_or_404(BookReview)
        form = AddBookReview()
        context = {"book": book, "form": form, "review": review}
        return render(request, "book.html", context)

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        review = get_list_or_404(BookReview)
        form = AddBookReview()
        context = {"book": book, "review": review, "form": form}
        if request.method == 'POST':
            form = AddBookReview(request.POST)
            if form.is_valid():
                text = request.POST.get('text')
                form = BookReview.objects.create(book_id=book, user=request.user, text=text)
                form.save()
                return redirect("book", pk=pk)
        return render(request, "book.html", context)


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author.html"


class BookAuthor(View):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        books = get_list_or_404(Book)
        context = {
            "books": books,
            "author": author,
        }
        return render(request, "books_list.html", context)


class AddBookForm(FormView):
    form_class = AddBook
    success_url = reverse_lazy('index')
    template_name = "add_book.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddAuthorForm(FormView):
    form_class = AddAuthor
    success_url = reverse_lazy('add_book')
    template_name = "add_author.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
