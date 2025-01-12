from tkinter import messagebox

class Book:
    def __init__(self, title, author_name, book_id):
        self.title = title
        self.author_name = author_name
        self.book_id = book_id
        self.student_id = None
        self.status=False

class Member:
    def __init__(self, student_id, book_title):
        self.student_id = student_id
        self.book_title = book_title

class Library:
    def __init__(self):
        self.book = {} 
        self.member = {}

    def add_book(self,book_id, title, author_name):
        self.book[title] = Book(title, author_name, book_id)

    def remove_book(self, title):
        if title in self.book:
            del self.book[title]
            return True
        else:
            return False

    def search_by_title(self, title):
     if title in self.book:
        book = self.book[title]
        msg = {
            "Title": book.title,
            "Author": book.author_name,
            "Book ID": book.book_id,
            "Student ID": book.student_id,
            "Status": "Available" if book.status else "Issued"
        }
        messagebox.showinfo("Success",msg)
     else:
        messagebox.showinfo("Success","Book not found in the library.")
    
    def search_by_author(self, author_name):
        author_books = [
            {
                "Title": book.title,
                "Author": book.author_name,
                "Book ID": book.book_id,
                "Student ID": book.student_id,
                "Status": "Available" if not book.status else "Issued"
            }
            for book in self.book.values() if book.author_name == author_name
        ]
        
        if author_books:
            print(f"Books by {author_name}:")
            for idx, book in enumerate(author_books, start=1):
                print(f"{idx}. Title: {book['Title']}, Book ID: {book['Book ID']}, Status: {book['Status']}")
            messagebox.showinfo("Success", author_books)
        else:
            messagebox.showinfo("Success", f"No books found by the author '{author_name}'.")
            return []

    def search_by_id(self, book_id):
        for book in self.book.values():
            if book.book_id == book_id:
                msg = {
                    "Title": book.title,
                    "Author": book.author_name,
                    "Book ID": book.book_id,
                    "Student ID": book.student_id,
                    "Status": "Available" if book.status else "Issued"
                }
        messagebox.showinfo("Success", msg)
   
    def issue_book(self, student_id, title):
        if title in self.book:
            book = self.book[title]
            if book.status:  # Check if the book is available
                book.student_id = student_id
                book.status = False
                messagebox.showinfo("Success", f"The book '{title}' has been successfully issued to Student ID: {student_id}.")
            else:
                messagebox.showinfo("Oops..", f"The book '{title}' is already issued to another student.")
        else:
            messagebox.showerror("Error", f"The book titled '{title}' does not exist in the library.")

example = Library()

    