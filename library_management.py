import datetime

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]  # Remove the book at the found index
                return  # Found and removed, we're done

        # If we reach here, the book wasn't found
        raise ValueError("Book with the given ISBN not found")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "available":
                    book.mark_borrowed()
                    return True  # Book borrowed successfully
                else:
                    return False  # Book already borrowed

        # Book not found
        raise ValueError("Book with the given ISBN not found")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "borrowed":
                    book.mark_returned()
                    return True  # Book returned successfully
                else:
                    return False  # Book wasn't borrowed

        # Book not found 
        raise ValueError("Book with the given ISBN not found")
