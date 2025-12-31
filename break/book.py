import random

books = []

def choose_book():
    if len(books) == 0:
        return None, None
    book = random.choice(books)
    page = random.randomint(1, 100)
    return book, page

def add_book(title):
    if title not in books:
        books.append(title)
        return True
    return False

def remove_book(title):
    if title in books:
        books.remove(title)
        return True
    return False

def update_book(old_title, new_title):
    if old_title in books:
        index = books.index(old_title)
        books[index] = new_title
        return True
    return False

def get_all_books():
    return books

def show_menu():
    print("Welcome to the Book Suggestion System!")
    print("1. Get Suggestions")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Update Book")
    print("5. Show all Books")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter option: ")

        if choice == "1":
            while True:
                book, page = choose_book()

                if book is None:
                    print("No books available.")
                    break

                print("Book for the Day:")
                print("Book Title:", book)
                print("Page:", page)

                again = input("Would you like another suggestion? (yes/no): ")
                if again != "yes":
                    break

        elif choice == "2":
            title = input("Enter the book title: ")
            if add_book(title):
                print("Book added successfully!")
            else:
                print("Book already exists!")

        elif choice == "3":
            title = input("Enter the book title to remove: ")
            if remove_book(title):
                print("Book removed successfully!")
            else:
                print("Book not found!")

        elif choice == "4":
            old = input("Enter the old title: ")
            new = input("Enter the new title: ")
            if update_book(old, new):
                print("Book updated successfully!")
            else:
                print("Book not found!")

        elif choice == "5":
            print("All Books:")
            for counter, book in enumerate(get_all_books(), start=1):
                print(f"{counter}. {book}")

        elif choice == "6":
            print("Thank you for using the Book Suggestion System!")
            break

        else:
            print("Invalid choice. Try again.")

main()

