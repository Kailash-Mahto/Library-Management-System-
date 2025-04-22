# inventory.py
import csv
import os

class Inventory:
    def __init__(self):
        self.file = 'data/books.csv'
        self.books = self.load_books()

    def load_books(self):
        books = []
        if os.path.exists(self.file):
            with open(self.file, newline='') as f:
                reader = csv.DictReader(f)
                books = list(reader)
        return books

    def save_books(self):
        with open(self.file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'author', 'copies'])
            writer.writeheader()
            writer.writerows(self.books)

    def menu(self):
        print("\n-- Manage Inventory --")
        print("1. Add Book")
        print("2. View Books")
        choice = input("Choose an option: ")
        if choice == '1':
            self.add_book()
        elif choice == '2':
            self.view_books()

    def add_book(self):
        book = {
            'id': input("Enter ID: "),
            'title': input("Enter Title: "),
            'author': input("Enter Author: "),
            'copies': input("Enter Copies: ")
        }
        self.books.append(book)
        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        for book in self.books:
            print(f"{book['id']} | {book['title']} | {book['author']} | Copies: {book['copies']}")

    def update_copies(self, book_id, delta):
        for book in self.books:
            if book['id'] == book_id:
                book['copies'] = str(int(book['copies']) + delta)
                self.save_books()
                return True
        return False

    def get_book(self, book_id):
        return next((b for b in self.books if b['id'] == book_id), None)