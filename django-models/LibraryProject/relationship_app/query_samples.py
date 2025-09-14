
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

orwell, _ = Author.objects.get_or_create(name="George Orwell")
austen, _ = Author.objects.get_or_create(name="Jane Austen")

book_1984, _ = Book.objects.get_or_create(title="1984", author=orwell)
book_af, _ = Book.objects.get_or_create(title="Animal Farm", author=orwell)
book_pp, _ = Book.objects.get_or_create(title="Pride and Prejudice", author=austen)

central, _ = Library.objects.get_or_create(name="Central Library")
west, _ = Library.objects.get_or_create(name="West Branch")

central.books.add(book_1984, book_af)
west.books.add(book_pp)

librarian_central, _ = Librarian.objects.get_or_create(name="Alice", library=central)
librarian_west, _ = Librarian.objects.get_or_create(name="Bob", library=west)

print("=== Data seeded ===")
print(f"Authors: {[a.name for a in Author.objects.all()]}")
print(f"Books:   {[b.title for b in Book.objects.all()]}")
print(f"Libraries: {[l.name for l in Library.objects.all()]}")
print()

print("1) All books by George Orwell:")
orwell_books = Book.objects.filter(author__name="George Orwell").values_list("title", flat=True)
print(list(orwell_books))
print()

print("2) All books in Central Library:")
central_books = central.books.values_list("title", flat=True)
print(list(central_books))
print()

print("3) Librarian for Central Library:")
print(central.librarian.name)
print("\n=== Done ===")
