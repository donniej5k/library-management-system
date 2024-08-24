Library Management System

Welcome to the Library Management System (LMS)! This command-line interface (CLI) application helps you manage a collection of books, users, and authors in a library. The system allows you to perform various operations such as adding books, borrowing and returning books, managing users, and handling author information.
Features

    Book Operations:
        Add a new book to the library.
        Borrow a book from the library.
        Return a borrowed book.
        Search for a book by its title.
        Display all books in the library.

    User Operations:
        Add a new user to the library system.
        View details of a specific user.
        Display a list of all users.

    Author Operations:
        Add a new author.
        View details of a specific author.
        Display a list of all authors.

How to Use
Prerequisites

    Ensure that you have Python 3 installed on your system.

Running the Program

    Clone the Repository:
        Clone the repository from GitHub to your local machine.
        If the repository is not yet on GitHub, you can create it by following GitHub's instructions on creating a new repository and pushing your local code to it.

    bash

git clone https://github.com/donniej5k/library-management-system.git
cd library-management-system

Run the Main Program:

    Navigate to the directory containing the files.
    Run the main.py script to start the Library Management System.

css

    python main.py

Using the CLI

    Main Menu:
        After running the program, you'll be greeted with the main menu, where you can choose from the following options:
            Book Operations
            User Operations
            Author Operations
            Quit

    Book Operations:
        Add a new book: Enter the details of the book (title, author, genre, publication date).
        Borrow a book: Provide the title of the book you want to borrow.
        Return a book: Enter the title of the book you are returning.
        Search for a book: Look for a specific book by its title.
        Display all books: View a list of all books in the library.

    User Operations:
        Add a new user: Input the user's name and library ID.
        View user details: Enter the library ID to view the user's details.
        Display all users: See a list of all users registered in the system.

    Author Operations:
        Add a new author: Input the author's name and biography.
        View author details: Enter the author's name to see their biography.
        Display all authors: View a list of all authors in the system.

    Quit:
        To exit the application, select the "Quit" option from the main menu.

Error Handling

The system includes basic error handling. If you enter invalid input or try to perform an operation on a non-existent item, the system will notify you and prompt you to try again.
Future Enhancements (Optional Bonus)

    Text File Handling: Implement file handling to load and save data for books, users, and authors.
    Reservation System: Add functionality for reserving books and notifying users when a reserved book becomes available.
    Fine Calculation: Implement fine calculation for overdue books, allowing users to pay fines.
