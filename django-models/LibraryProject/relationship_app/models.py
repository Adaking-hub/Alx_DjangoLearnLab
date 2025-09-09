from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    # One-to-Many: many books can belong to one author
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    # Many-to-Many: a library can have many books, and a book can belong to many libraries
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # One-to-One: each library has exactly one librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name