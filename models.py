import datetime
class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.status = "available"
        self.borrowed_date = None  # Initially not borrowed

    def mark_borrowed(self):
        self.status = "borrowed"
        self.borrowed_date = datetime.date.today()

    def mark_returned(self):
        self.status = "available"
        self.borrowed_date = None  # Clear borrowed date upon return