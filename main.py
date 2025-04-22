# main.py
from inventory import Inventory
from issue_return import IssueReturn
from analytics import Analytics
# from logs import Logger

def main():
    inventory = Inventory()
    issue_return = IssueReturn(inventory)
    analytics = Analytics(inventory)
    # logger = Logger()

    while True:
        print("\n--- Library Management System ---")
        print("1. Manage Book Inventory")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Usage Stats")
        #print("5. Export Logs")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            inventory.menu()
        elif choice == '2':
            issue_return.issue_book()
        elif choice == '3':
            issue_return.return_book()
        elif choice == '4':
            analytics.show_stats()
        # elif choice == '5':
        #     logger.export_logs()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
    