# issue_return.py
import csv
import datetime

class IssueReturn:
    def __init__(self, inventory):
        self.inventory = inventory
        self.file = 'data/transactions.csv'

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        user = input("Enter Borrower Name: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        if self.inventory.update_copies(book_id, -1):
            with open(self.file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([book_id, user, datetime.date.today(), due_date, 'issued'])
            print("Book issued.")
        else:
            print("Book not found or unavailable.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        user = input("Enter Borrower Name: ")
        return_date = datetime.date.today()
        fine = self.calculate_fine(book_id, user, return_date)
        if fine > 0:
            print(f"Late fine: ₹{fine}")
        self.inventory.update_copies(book_id, 1)
        with open(self.file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([book_id, user, return_date, return_date, 'returned'])
        print("Book returned.")

    def calculate_fine(self, book_id, user, return_date):
        with open(self.file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == book_id and row[1] == user and row[4] == 'issued':
                    due_date = datetime.datetime.strptime(row[3], '%Y-%m-%d').date()
                    if return_date > due_date:
                        delta = (return_date - due_date).days
                        return delta * 5  # ₹5 per day
        return 0