from classes.book import Book

class User:
    def __init__(self, user_id: str, name: str, borrowed_books: list[Book]):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        for i in range(len(self.borrowed_books)):
            if self.borrowed_books[i] == book:
                self.borrowed_books.pop(i)
















