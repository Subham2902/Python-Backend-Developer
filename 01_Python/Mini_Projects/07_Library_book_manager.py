books = []


def add_book():
    book = input("Enter book name: ")
    books.append(book)
    print("Book added successfully!\n")


def view_books():
    if len(books) == 0:
        print("Library is empty.\n")
    else:
        print("\nBooks in Library:")
        for i in range(len(books)):
            print(f"{i + 1}. {books[i]}")
        print()


def search_book():
    book = input("Enter book name to search: ")

    if book in books:
        print("Book found!\n")
    else:
        print("Book not found.\n")


def remove_book():
    book = input("Enter book name to remove: ")

    if book in books:
        books.remove(book)
        print("Book removed successfully!\n")
    else:
        print("Book not found.\n")


while True:
    print("===== Library Book Manager =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        remove_book()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.\n")