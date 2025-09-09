# create
from myapp.models import Book  

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

print (book)

# retrieve book command

from bookshelf.models import Book

book = Book.objects.get(id=1)   # use the correct id from your DB
print(book.title, book.author, book.publication_year)

# Expected retrieve Output
1984 by George Orwell 1949

# update  

from bookshelf.models import Book

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Expected output for update
Nineteen Eighty-Four

# delete

from bookshelf.models import Book

book.delete()

# Expected output
(1, {'library.Book': 1})   # Output after deletion

<QuerySet []>