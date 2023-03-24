# This is a basic Library Management System created for private collectors to be able to categorise their books.
# Developed by: Insiyah Rangwala (Student ID: S22003116, MSc Data Science in Business at Regent's University London.
# Developed for DSB706 - Coding module at Regent's University London, taught by Neda Ahmedi.

#Class definition of Books, with unique variables representing the unique identifier, title, author name, year of publication, and location of the book respectively.
class Book:
    def __init__(self, book_id, title, author, year, isbn, location):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.location = location

#Class definition of the library and different functions of the library: displaying all the books in the library, adding to the library, searching the library, and removing books from the library.
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(f"{book.book_id} - {book.title} by {book.author}, published by {book.year}. ISBN-13 code: {book.isbn}, Location: {book.location}")

if __name__ == "__main__":
    library = Library()

    # Initial list of books in the library.
    library.add_book(Book(1, "Pride and Prejudice", "Jane Austen", 1812, 9781908533050, "Dubai"))
    library.add_book(Book(2, "The Priory of the Orange Tree", "Samantha Shannon", 2018, 9781635570281, "London"))
    library.add_book(Book(3, "A Day of Fallen Night", "Samantha Shannon", 2023, 9781635577921, "London"))
    library.add_book(Book(4, "A Gentleman in Moscow", "Amor Towles", 2016, 9780099558781, "Dubai"))
    library.add_book(Book (5, "To Sleep in a Sea of Stars", "Christopher Paolini", 2020, 9781529046526, "London"))
    print(f"There are {len(library.books)} books in the library")

    #Menu that is shown when the program is run.
    while True:
        print("\nLibrary Management System")
        print("------------------------")
        print("1. Display all books")
        print("2. Add new book")
        print("3. Search book")
        print("4. Remove book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        #Displaying all the books in the library.
        if choice == 1:
            library.display_books()

        #Adding new books to the library.
        elif choice == 2:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book's year of publication: "))
            isbn = int(input("Enter book's ISBN-13 code: "))
            location = input("Enter book location: ")
            library.add_book(Book(len(library.books) + 1, title, author, year, isbn, location))
            print("Book added successfully")

        #Searching for a book in the library.
        elif choice == 3:
            title = input("Enter book title: ")
            book = library.search_book_by_title(title)
            if book:
                print(f"Book found: {book.title} by {book.author}")
            else:
                print(f"Book with title '{title}' not found")

        #Removing a book from the library.
        elif choice == 4:
            book_id = int(input("Enter book ID: "))
            if library.remove_book(book_id):
                print(f"Book with ID {book_id} removed successfully")
            else:
                print(f"Book with ID {book_id} not found in the library")

        #Exiting the program.
        elif choice == 5:
            print("Exiting the program")
            break

        else:
            print("Invalid choice")
