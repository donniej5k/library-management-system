# main.py

from book import Book
from user import User
from author import Author

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    # Implementing the actions for each menu
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        genre = input("Enter the genre: ")
        publication_date = input("Enter the publication date: ")
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def borrow_book(self):
        title = input("Enter the book title to borrow: ")
        for book in self.books:
            if book.get_title() == title:
                if book.borrow():
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"Sorry, '{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found.")

    def return_book(self):
        title = input("Enter the book title to return: ")
        for book in self.books:
            if book.get_title() == title:
                book.return_book()
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self):
        title = input("Enter the book title to search: ")
        for book in self.books:
            if book.get_title() == title:
                availability = "Available" if book.is_available() else "Borrowed"
                print(f"Book found: {book.get_title()} by {book.get_author()} ({book.get_genre()}, {book.get_publication_date()}) - {availability}")
                return
        print(f"Book '{title}' not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("All Books:")
            for book in self.books:
                availability = "Available" if book.is_available() else "Borrowed"
                print(f"{book.get_title()} by {book.get_author()} ({book.get_genre()}, {book.get_publication_date()}) - {availability}")

    def add_user(self):
        name = input("Enter the user's name: ")
        library_id = input("Enter the user's library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"User '{name}' added successfully.")

    def view_user_details(self):
        library_id = input("Enter the user's library ID: ")
        for user in self.users:
            if user.get_library_id() == library_id:
                print(f"User Details: Name: {user.get_name()}, ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books()) or 'None'}")
                return
        print(f"User with ID '{library_id}' not found.")

    def display_all_users(self):
        if not self.users:
            print("No users available.")
        else:
            print("All Users:")
            for user in self.users:
                print(f"Name: {user.get_name()}, ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books()) or 'None'}")

    def add_author(self):
        name = input("Enter the author's name: ")
        biography = input("Enter the author's biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter the author's name: ")
        for author in self.authors:
            if author.get_name() == name:
                print(f"Author Details: Name: {author.get_name()}, Biography: {author.get_biography()}")
                return
        print(f"Author '{name}' not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
        else:
            print("All Authors:")
            for author in self.authors:
                print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")

if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.main_menu()
