from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ISBN(models.Model):
    author = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.isbn_number

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
