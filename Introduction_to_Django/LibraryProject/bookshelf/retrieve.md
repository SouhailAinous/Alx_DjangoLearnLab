from bookshelf.models import Book
b = Book.objects.first()
b.title, b.author, b.publication_year  
# expected output: ('1984', 'George Orwell', 1949)
