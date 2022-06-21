from django import forms
from .models import Book, Author


class AddBook(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    released_year = forms.IntegerField(max_value=9999, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "rows": 3}))
    class Meta:
        model = Book
        fields = ["title", "released_year", "description", "author_id"]


class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "age"]
