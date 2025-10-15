"""

Single Responsibility Principle (SRP)

A class should have one, and only one, reason to change.
Each class should focus on a single task or functionality.

"""

"""

This particular class violates the single responsibility principle.
LibrarySystem class handles multiple responsibilities.

 SRP Violation
 
    1.Manages books.
    2.Takes user input.
    3. Displays output.
        
This violates the SRP, which states that a class should have only one reason to change or one responsibility.

"""


class LibrarySystem:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book):
        self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def input_book(self):
        book = input("Enter book title: ")
        self.add_book(book)

    def remove_book(self):
        book = input("Enter book title to remove: ")
        self.delete_book(book)


# ===============================================================================#

"""

Refactor Solution

The BookManager class handles the storage and management of books.
BookPresenter is responsible for displaying the list of books.
BookInput handles user input for adding and removing books.

This refactoring adheres to the Single Responsibility Principle,
as each class now has a clearly defined and distinct responsibility.
This separation makes the code easier to maintain, test, and extend
in the future.

"""


# This is responsible for managing the book collection
class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book):
        self.books.remove(book)

    def get_books(self):
        return self.books


# This is responsible for displaying the books
class BookPresenter:
    @staticmethod
    def display_books(books):
        for book in books:
            print(f"- {book}")


# This is responsible for handling user input
class BookInput:
    @staticmethod
    def input_book():
        return input("Enter book title: ")

    @staticmethod
    def remove_book():
        return input("Enter book title to remove: ")
