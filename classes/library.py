from classes.book import Book
from classes.user import User
from classes.logger import Logger
from classes.system_asmin import SistemAdmin

class Library:
    max_borrow_days: int = 14
    def __init__(self, books: dict[str, Book], users: dict[str, User]):
        self.books = books
        self.users = users

    def register_user(self, user: User) -> None:
        self.users.update({user.user_id: user})

    def add_book(self, book: Book):
        self.books.update({book.isbn: book})

    def perform_borrow(self, user_id: str, isbn: str) -> None:
        if user_id in self.users:
            if isbn in self.books:
                book = self.books[isbn]
                if book.is_available:
                    self.users[user_id].borrow_book(book)
                    book.is_available = False
                    Logger.log_action("BORROW", f"{self.users[user_id].user_id, book.isbn}")
                    SistemAdmin.update_transactions_count()
                else:
                    raise "The book is not available."
            else:
                raise "The book is not found."
        else:
            raise "The user is not found."

    def perform_return(self, user_id: str, isbn: str) -> None:
        if user_id in self.users:
            if isbn in self.books:
                user = self.users[user_id]
                book = self.books[isbn]
                if not book.is_available:
                    if book in user.borrowed_books:
                        user.return_book(book)
                        book.is_available = True
                        Logger.log_action("RETURN", f"{user.user_id, book.isbn}")
                    else:
                        raise "The book is not on loan to the user."
                else:
                    raise "The book is not borrowed."
            else:
                raise "The book is not found."
        else:
            raise "The user is not found."






