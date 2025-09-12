from bookshelf.models import Book
b = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
b.title = "Nineteen Eighty-Four"
b.save()
b.title  
# expected output: "Nineteen Eighty-Four"
