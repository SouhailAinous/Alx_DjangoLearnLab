from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949)
b.delete()
Book.objects.all().count()  
# expected output: 0
