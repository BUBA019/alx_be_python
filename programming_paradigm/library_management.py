# library_management.py

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        """Add a book to the library"""
        self.books.append({"title": title, "author": author})
        return f"Book '{title}' by {author} added."

    def remove_book(self, title):
        """Remove a book by title"""
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                return f"Book '{title}' removed."
        return f"Book '{title}' not found."

    def search_book(self, title):
        """Search for a book by title"""
        for book in self.books:
            if book["title"].lower() == title.lower():
                return f"Found: '{book['title']}' by {book['author']}"
        return f"Book '{title}' not found."

    def display_books(self):
        """Display all books in the library"""
        if not self.books:
            return "No books in the library."
        result = "Books in the library:\n"
        for i, book in enumerate(self.books, start=1):
            result += f"{i}. '{book['title']}' by {book['author']}\n"
        return result.strip()


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            print(library.add_book(title, author))
        elif choice == "2":
            title = input("Enter book title to remove: ")
            print(library.remove_book(title))
        elif choice == "3":
            title = input("Enter book title to search: ")
            print(library.search_book(title))
        elif choice == "4":
            print(library.display_books())
        elif choice == "5":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
