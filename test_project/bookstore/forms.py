from django import forms
from .models import Book


# class AddBook(forms.Form):
#     title = forms.CharField(max_length=250, label="Title")


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "released_year", "description", "author_id",]

