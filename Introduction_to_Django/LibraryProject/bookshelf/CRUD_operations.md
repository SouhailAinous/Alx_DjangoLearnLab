# CRUD Operations

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # expected output: <Book: Book object (1)> (id may vary)
## Retrieve 
from bookshelf.models import Book
b = Book.objects.first()
b.title, b.author, b.publication_year  
# expected output: ('1984', 'George Orwell', 1949)
## Update 
from bookshelf.models import Book
b = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
b.title = "Nineteen Eighty-Four"
b.save()
b.title  
# expected output: "Nineteen Eighty-Four"
## Delete
from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949)
b.delete()
Book.objects.all().count()  
# expected output: 0
