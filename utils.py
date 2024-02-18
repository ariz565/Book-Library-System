def search_books(query, search_by="title"):
    query = query.lower()
    if search_by == "title":
        return Book.query.filter(Book.title.like(f'%{query}%')).all() 
    elif search_by == "author":
        return Book.query.filter(Book.author.like(f'%{query}%')).all() 
    elif search_by == "publication_year":
        return Book.query.filter(Book.publication_year == query).all() 
    else:
        return []  
