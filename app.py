from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource, reqparse
from models import Book, db
from utils import search_books  

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

# Create database schema - Execute once initially, then comment out
with app.app_context():
    db.create_all()

class BookList(Resource):
    def get(self):
        books = Book.query.all()
        books_data = [
            {"title": book.title, "author": book.author, "isbn": book.isbn,
             "publication_year": book.publication_year, "status": book.status}
            for book in books
        ]
        return jsonify(books_data)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, required=True)
        parser.add_argument("author", type=str, required=True)
        parser.add_argument("isbn", type=str, required=True)
        parser.add_argument("publication_year", type=int, required=True)
        args = parser.parse_args()

        new_book = Book(args["title"], args["author"], args["isbn"], args["publication_year"])
        db.session.add(new_book)
        db.session.commit()
        return new_book.__dict__, 201 

class Book(Resource):
    def get(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            return book.__dict__, 200
        abort(404, message="Book not found")

    def delete(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return '', 204 
        abort(404, message="Book not found")

    def put(self, isbn):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('author')
        parser.add_argument('publication_year', type=int)
        args = parser.parse_args()

        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            if args['title']:
                book.title = args['title']
            if args['author']:
                book.author = args['author']
            if args['publication_year']:
                book.publication_year = args['publication_year']
            db.session.commit() 
            return {"message": "Book updated"}, 200
        abort(404, message="Book not found")

# ... (Implement BorrowBook, ReturnBook, SearchBooks - Similar structure, using database interaction)
class BorrowBook(Resource):
    def post(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            try:
                book.borrow()
                db.session.commit()  # Save the updated status
                return {"message": "Book borrowed successfully"}, 200
            except ValueError as e:
                return {"message": str(e)}, 400 
        abort(404, message="Book not found") 

class ReturnBook(Resource):
    def post(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            try:
                book.return_book()
                db.session.commit()  # Save the updated status
                return {"message": "Book returned successfully"}, 200
            except ValueError as e:
                return {"message": str(e)}, 400 
        abort(404, message="Book not found") 

class SearchBooks(Resource):
    def get(self):
        query = request.args.get("query")
        search_by = request.args.get("search_by", "title")
        if not query:
            return {"message": "Missing query parameter"}, 400
        if search_by not in ["title", "author", "publication_year"]:
            return {"message": "Invalid search_by parameter"}, 400

        results = search_books(query, search_by)  # Make sure your search_books interacts with the database 
        return jsonify([book.__dict__ for book in results])
# API Resource Routing (no changes needed)
api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<isbn>')
api.add_resource(BorrowBook, '/books/<isbn>/borrow')
api.add_resource(ReturnBook, '/books/<isbn>/return')
api.add_resource(SearchBooks, '/books/search')


if __name__ == "__main__":
    app.run(debug=True)
