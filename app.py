from flask import Flask, jsonify, request
from models import Book
from library_management import Library
from search import search_by_title, search_by_author, search_by_publication_year

app = Flask(__name__)
library = Library()  # Instance of our library

# Add dummy data (remove this when connecting to a database)
library.add_book(Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227", 1937))
library.add_book(Book("Pride and Prejudice", "Jane Austen", "978-0141439518", 1813))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960))
library.add_book(Book("Flask", "Python", "123-4567899999", 2024))


@app.route('/books', methods=['POST', 'GET'])
def book_crud():
    if request.method == 'POST':
        data = request.get_json()
        new_book = Book(data['title'], data['author'], data['isbn'], data['publication_year'])
        library.add_book(new_book)
        return jsonify({"message": "Book added successfully"}), 201

    else:  # GET
        available_books = [book.__dict__ for book in library.books if book.status == "available"]
        return jsonify(available_books)

@app.route('/books/<isbn>', methods=['PUT'])
def update_book_status(isbn):
    action = request.args.get('action') 
    if action == 'borrow':
        success = library.borrow_book(isbn)
        if success:
            return jsonify({"message": "Book borrowed successfully"}), 200
        else:
            return jsonify({"message": "Book unavailable or not found"}), 400 

    elif action == 'return':
        success = library.return_book(isbn)
        if success:
            return jsonify({"message": "Book returned successfully"}), 200
        else:
            return jsonify({"message": "Book not found or was not borrowed"}), 400
    else:
        return jsonify({"message": "Invalid action"}), 400

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')
    author = request.args.get('author')
    year = request.args.get('year')

    results = []
    if title:
        results = search_by_title(library.books, title)
    if author:
        results = search_by_author(library.books, author)
    if year:
        try:
            results = search_by_publication_year(library.books, int(year)) 
        except ValueError:
            return jsonify({"message": "Invalid publication year"}), 400

    # Serialize book objects to dictionaries before returning
    book_dicts = [book.__dict__ for book in results] 
    return jsonify(book_dicts) 

@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    try:
        library.remove_book(isbn)
        return jsonify({"message": "Book removed successfully"}), 200
    except ValueError:
        return jsonify({"message": "Book not found"}), 400


@app.route('/overdue', methods=['GET'])
def get_overdue():
    overdue_books = library.get_overdue_books()
    overdue_list = [book.__dict__ for book in overdue_books]
    return jsonify(overdue_list)

if __name__ == '__main__':
    app.run(debug=True)
