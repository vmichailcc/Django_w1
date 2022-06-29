from django.contrib import admin
from .models import Book, Author, BookReview
# Register your models here.

admin.site.register(BookReview)


class AuthorAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'age')


class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
    search_fields = ["title", "description", "author_id"]
    list_filter = ["title", "author_id"]
    list_editable = ["title", "description"]
    radio_fields = {"author_id": admin.HORIZONTAL}


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
