from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize the database

class Book(db.Model):
    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publication_year = db.Column(db.Integer)
    status = db.Column(db.String(20), default="available")

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            db.session.commit()  
        else:
            raise ValueError("Book is not available")

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            db.session.commit() 
        else:
            raise ValueError("Book is already available")
        
class Library:
    def __init__(self):
        pass  # No more internal books list

    def add_book(self, book):
        db.session.add(book)
        db.session.commit()

    def remove_book(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()  # Query the database
        if book:
            db.session.delete(book)
            db.session.commit()
        else:
            raise ValueError("Book not found")
