from django.db import models
from authors.models import Author
from categories.models import Category

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
