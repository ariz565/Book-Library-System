import pytest
from library_management import Library, search_by_title, search_by_author, search_by_publication_year
from models import Book
import datetime

# Fixtures - Help us create common test data 
@pytest.fixture
def new_book():
    return Book("Cracking the Interview", "MCDOWELL", "777-4555451200", 2010)

@pytest.fixture
def library_with_books():
    library = Library()
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227", 1937))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", "978-0141439518", 1813))
    library.add_book(Book("Flask", "Python", "123-4567899999", 2024)) 
    return library

@pytest.fixture
def library_with_books():
    library = Library()  # Instantiate the library
    library.add_book(Book("The Hobbit", "J.R.R Tolkien", 1937))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", 1813)) 
    return library 

# TEST CASES: 
def test_add_book():
    library = Library()
    new_book = Book("A Game of Thrones", "George R.R. Martin", "978-0553103540", 1996)
    library.add_book(new_book)
    assert len(library.books) == 1
    assert new_book in library.books

def test_remove_book(library_with_books): 
    book_to_remove = library_with_books.books[0]  # Take the first book
    library_with_books.remove_book(book_to_remove.isbn)
    assert len(library_with_books.books) == 1  # Remaining size
    assert book_to_remove not in library_with_books.books 

def test_remove_nonexistent_book(library_with_books):
    with pytest.raises(ValueError): 
        library_with_books.remove_book("978-1234567890") 

def test_borrow_book(library_with_books, new_book):
    library_with_books.add_book(new_book) 
    success = library_with_books.borrow_book(new_book.isbn)
    assert success
    assert new_book.status == "borrowed" 
    assert new_book.borrowed_date is not None  # Should be populated 

def test_borrow_already_borrowed(library_with_books):
    book = library_with_books.books[0]
    library_with_books.borrow_book(book.isbn)  # Already borrowed
    success = library_with_books.borrow_book(book.isbn)  # Try again
    assert not success

def test_return_book(library_with_books):  
    # First, simulate borrowing
    book = library_with_books.books[1]
    library_with_books.borrow_book(book.isbn)
    # Now, test the return
    success = library_with_books.return_book(book.isbn)
    assert success
    assert book.status == "available"
    assert book.borrowed_date is None  # Should be reset

def test_search_by_title(library_with_books): 
    results = search_by_title(library_with_books.books, "Hobbit")
    assert len(results) == 1 
    assert results[0].title == "The Hobbit" 

def test_search_by_author(library_with_books):
    results = search_by_author(library_with_books.books, "Austen")
    assert len(results) == 1
    assert results[0].author == "Jane Austen"

def test_search_by_publication_year(library_with_books):
    results = search_by_publication_year(library_with_books.books, 1937)
    assert len(results) == 1 
    assert results[0].title == "The Hobbit"  # Assuming it's the only book from 1937