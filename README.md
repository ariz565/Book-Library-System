# Book Library System
## _Manage your library with ease using a RESTful API built with Flask._


This project implements a Flask REST API to manage a book library. It includes features for adding, listing available books, borrowing/returning books, searching, and viewing overdue books.


## Features

* **CRUD Operations:**
    * Create new book listings *(POST /books).*
    * Retrieve available books *(GET /books)*.
    * Update book status (borrowed/returned) *(PUT /books/<isbn>)*.
    * Delete book entries *(DELETE /books/<isbn>).*

* **Search Functionality:**
    * Search books by title, author, or publication year _(GET /search)._

* **Overdue Book Tracking:**
    * Retrieve a list of overdue books _(GET /overdue)_

## Structure
    * app.py: Contains the core Flask application logic and API routes.
    * models.py: Defines the Book model representing book data.
    * library_management.py: Houses library logic (adding, borrowing, returning, etc.).
    * search.py: Encapsulates the search functions.
    * test_api.py: For testing
    
## API Reference
List Available Books:

```sh
GET http://127.0.0.1:5000/books 
```

Add a New Book:

```sh
POST http://127.0.0.1:5000/books 
Content-Type: application/json
{
    "title": "New Book Title",
    "author": "Book Author",
    "isbn": "978-1234567890",
    "publication_year": 2023
} 
```
Search Books:

```sh
GET http://127.0.0.1:5000/search?title=Pride 
GET http://127.0.0.1:5000/search?author=Austen 
GET http://127.0.0.1:5000/search?year=1960 
```



Book Status Management:
```sh
# Update existing book details
PUT http://127.0.0.1:5000/books/978-1234567890 
Content-Type: application/json

{
     "title": "The Hobbit (Revised Edition)", 
     "publication_year": 1951
}

# Mark a book as borrowed
PUT http://127.0.0.1:5000/books/978-0141439518?action=borrow 

# Mark a book as returned
PUT http://127.0.0.1:5000/books/978-0547928227?action=return 

# Get overdue books
GET http://127.0.0.1:5000/overdue 

```



    


## Getting Started
* Python 3.x 
* Flask ( pip install flask)
* For persistent storage, you'll need a database (such as SQLite, PostgreSQL, or MySQL) and a corresponding ORM (like SQLAlchemy) to interact with it.



## Project Setup

1. Clone the repository:
    ```sh
        https://github.com/ariz565/Book-Library-System.git
    ```
2. Create Virtual Environment
    ```sh
    python -m venv env 
    source env/bin/activate  # Linux/macOS 
    env\Scripts\activate  # Windows 
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the application
    ```sh
    python app.py
    flask --app app run
    flask run 
    ```
**This will start the Flask development server. Access the API through your browser or a tool like Postman (usually at http://127.0.0.1:5000/)**

**Unit Testing:** 
```sh
pip install pytest
```
Open terminal run the command : pytest



**Notes:**
The current implementation uses placeholder data. Consider database integration.
The overdue books feature assumes due date tracking logic .







