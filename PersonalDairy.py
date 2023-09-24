#Personal Dairy
import os
import datetime

def create_entry():
    entry = input("Write your entry: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_with_timestamp = f"{timestamp}\n{entry}\n"

    return entry_with_timestamp

def save_entry(entry):
    with open("diary.txt", "a") as file:
        file.write(entry)

def view_entries():
    if not os.path.exists("diary.txt"):
        print("No entries found.")
        return

    with open("diary.txt", "r") as file:
        entries = file.read()

    print("Previous entries:\n")
    print(entries)

def diary_menu():
    print("Welcome to Your Personal Diary!")
    print("1. Write an entry")
    print("2. View previous entries")
    print("3. Quit")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            entry = create_entry()
            save_entry(entry)
            print("Entry saved successfully!")
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Thank you for using the diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

diary_menu()