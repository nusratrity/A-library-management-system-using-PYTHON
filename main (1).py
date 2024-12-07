import datetime

# Sample data storage
books = []
members = []
borrowed_books = []

# Function to display menu
def display_menu():
    print("\n====== Library Management System ======")
    print("1. Add a New Book")
    print("2. View All Books")
    print("3. Update Book Details")
    print("4. Remove a Book")
    print("5. Add a New Member")
    print("6. View All Members")
    print("7. Borrow a Book")
    print("8. Return a Book")
    print("9. Exit")
    print("=======================================")

# Function to add a new book
def add_book():
    print("\n--- Add a New Book ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Number of Copies: "))
    books.append({"id": book_id, "title": title, "author": author, "copies": copies})
    print(f"Book '{title}' added successfully!")

# Function to view all books
def view_books():
    print("\n--- All Books ---")
    if not books:
        print("No books available!")
    else:
        for book in books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")

# Function to update book details
def update_book():
    print("\n--- Update Book Details ---")
    book_id = input("Enter the Book ID to update: ")
    for book in books:
        if book["id"] == book_id:
            book["title"] = input("Enter New Title: ")
            book["author"] = input("Enter New Author: ")
            book["copies"] = int(input("Enter New Number of Copies: "))
            print("Book details updated successfully!")
            return
    print("Book not found!")

# Function to remove a book
def remove_book():
    print("\n--- Remove a Book ---")
    book_id = input("Enter the Book ID to remove: ")
    global books
    books = [book for book in books if book["id"] != book_id]
    print("Book removed successfully!")

# Function to add a new member
def add_member():
    print("\n--- Add a New Member ---")
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    members.append({"id": member_id, "name": name})
    print(f"Member '{name}' added successfully!")

# Function to view all members
def view_members():
    print("\n--- All Members ---")
    if not members:
        print("No members found!")
    else:
        for member in members:
            print(f"ID: {member['id']}, Name: {member['name']}")

# Function to borrow a book
def borrow_book():
    print("\n--- Borrow a Book ---")
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["copies"] > 0:
                book["copies"] -= 1
                borrowed_books.append({
                    "member_id": member_id,
                    "book_id": book_id,
                    "borrowed_date": datetime.date.today()
                })
                print(f"Book '{book['title']}' borrowed successfully!")
                return
            else:
                print("No copies available!")
                return
    print("Book not found!")

# Function to return a book
def return_book():
    print("\n--- Return a Book ---")
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    for record in borrowed_books:
        if record["member_id"] == member_id and record["book_id"] == book_id:
            borrowed_books.remove(record)
            for book in books:
                if book["id"] == book_id:
                    book["copies"] += 1
                    print(f"Book '{book['title']}' returned successfully!")
                    return
    print("Borrow record not found!")

# Main Program
def library_system():
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            update_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            add_member()
        elif choice == '6':
            view_members()
        elif choice == '7':
            borrow_book()
        elif choice == '8':
            return_book()
        elif choice == '9':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the Library System
library_system()
