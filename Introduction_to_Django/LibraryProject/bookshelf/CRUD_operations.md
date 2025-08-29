# create
from myapp.models import Book  

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

print (book)

# retrieve
book = Book.objects.get(id=1)   # use the correct id from your DB
print(book.title, book.author, book.publication_year)

# update
book.title = "Things Fall Apart - Updated"
book.save()
print(book.title)

# delete
book.delete()