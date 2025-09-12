from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949)
book.delete()
Book.objects.all().count()  
# expected output: 0