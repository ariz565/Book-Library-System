def search_by_title(books, title):
    title = title.lower() 
    return [book for book in books if title in book.title.lower()]

def search_by_author(books, author):
    author = author.lower()  
    return [book for book in books if author in book.author.lower()]

def search_by_publication_year(books, year):
    return [book for book in books if book.publication_year == year] 
