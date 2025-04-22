# analytics.py
import csv
from collections import Counter

class Analytics:
    def __init__(self, inventory):
        self.inventory = inventory
        self.transaction_file = 'data/transactions.csv'

    def show_stats(self):
        print("\n-- Library Usage Stats --")
        print(f"Total Books: {len(self.inventory.books)}")

        issued_books = 0
        count = Counter()
        with open(self.transaction_file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[4] == 'issued':
                    issued_books += 1
                    count[row[0]] += 1

        print(f"Currently Issued Books: {issued_books}")
        print("Most Borrowed Books:")
        for book_id, times in count.most_common(5):
            book = self.inventory.get_book(book_id)
            if book:
                print(f"{book['title']} - {times} times")
