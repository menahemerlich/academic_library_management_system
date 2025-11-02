from classes.book import Book
from classes.user import User
from classes.library import Library
from classes.system_asmin import SistemAdmin

book_1 = Book("hary", "b.ben", "001")
book_2 = Book("hello", "a.dog", "002")
book_3 = Book("mi any", "m.lev", "003")
user_1 = User("322", "Erlich", [])
user_2 = User("320", "Etty", [])
books = {}
users = {}
library_1 = Library(books, users)
library_1.register_user(user_1)
library_1.register_user(user_2)
library_1.add_book(book_1)
library_1.add_book(book_2)
library_1.add_book(book_3)
library_1.perform_borrow("322", "001")
print(user_1.borrowed_books[0].isbn)
print(SistemAdmin.total_transactions)
library_1.perform_borrow("322", "002")
print(user_1.borrowed_books[1].isbn)
print(SistemAdmin.total_transactions)


