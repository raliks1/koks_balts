class Book:
    def __init__(self, title, author, isbn, is_checked_out=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

class LibraryMember:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = list(borrowed_books) if borrowed_books is not None else []

class Library:
    