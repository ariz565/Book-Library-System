import datetime

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                return
        raise ValueError("Book Removed Successfully")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "available":
                    book.mark_borrowed()  # Mark the book as borrowed
                    return True
                else:
                    return False
        raise ValueError("Book with the given ISBN not found")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "borrowed":
                    book.mark_returned()  # Mark the book as returned
                    return True
                else:
                    return False
        raise ValueError("Book with the given ISBN not found")

    def get_overdue_books(self, loan_period_days=14):
        overdue_books = []
        today = datetime.date.today()
        for book in self.books:
            if book.status == "borrowed":
                due_date = book.borrowed_date + datetime.timedelta(days=loan_period_days)
                if due_date < today:
                    overdue_books.append(book)
        return overdue_books

