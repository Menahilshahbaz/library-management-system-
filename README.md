# PROJECT OVERVIEW
This project is a Library Management System built with Python using the Tkinter library for the graphical user interface (GUI). It allows users to manage books and members, providing features for adding, searching, issuing, and removing books, as well as tracking book status.

                                                        GUI FILE:
                                                        
This file contains the graphical user interface for the system. Its features include:
### Adding Books:
Opens a dialog box for the user to input the book's ID, title, and author's name.
Saves the book details in the library database.
### Removing Books:
Prompts the user to input the book title.
Removes the book if it exists in the library database.
### Issuing Books to Members:
Opens a dialog box to enter the student ID and book title.
Issues the book to the student if it is available.
### Searching Books:
Prompts the user to search by title, book ID, or author.
Displays the details of the books matching the query.

                                                         MAIN FILE:
                                                         
In main file the core functionality of the library system, including managing books and member records. It defines three main classes:
### Book:
Represents a book with attributes for the title, author name, book ID, student ID (if issued), and status (available or issued).
### Member:
Represents a member with attributes for student ID and the title of the book they borrowed.
### Library:
Acts as the system's backend to manage books and members.

                                                       


