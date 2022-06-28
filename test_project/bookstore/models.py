from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name="Title")
    released_year = models.IntegerField(verbose_name="Released year")
    description = models.TextField(max_length=5000, verbose_name="Description")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE, verbose_name="Author")


    def __str__(self):
        return self.title




class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
