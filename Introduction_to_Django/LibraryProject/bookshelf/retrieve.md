from bookshelf.models import Book

book = Book.objects.get(id=1)   # use the correct id from your DB
print(book.title, book.author, book.publication_year)