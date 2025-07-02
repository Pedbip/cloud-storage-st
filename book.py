import requests

def get_books():
    req = requests.get('https://api.potterdb.com/v1/books')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch books: {req.status_code}")
    
def get_book_by_id(book_id):
    req = requests.get(f'https://api.potterdb.com/v1/books/{book_id}')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch book with ID {book_id}: {req.status_code}")

# Not using functions above, but keeping them for completeness
def get_book_chapters(book_id):
    req = requests.get(f'https://api.potterdb.com/v1/books/{book_id}/chapters')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch chapters for book ID {book_id}: {req.status_code}")
    
def get_book_chapter_by_id(book_id, chapter_id):
    req = requests.get(f'https://api.potterdb.com/v1/books/{book_id}/chapters/{chapter_id}')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch chapter {chapter_id} for book ID {book_id}: {req.status_code}")