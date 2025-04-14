import pickle
import os

# -----------------------------
# Personal Library Manager App
# -----------------------------
class LibraryManager:
    def __init__(self, filename="library.pkl"):
        self.books = []
        self.filename = filename
        self.load_library()

    def save_library(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.books, f)

    def load_library(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.books = pickle.load(f)

    def add_book(self):
        print("\n📘 Add a New Book:")
        title = input("Enter title: ")
        author = input("Enter author: ")
        try:
            year = int(input("Enter publication year: "))
        except ValueError:
            print("⚠️ Invalid year. Setting to 0.")
            year = 0
        genre = input("Enter genre: ")
        read_input = input("Have you read this book? (y/n): ").strip().lower()
        read = read_input == 'y'

        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read
        }

        self.books.append(book)
        self.save_library()
        print("✅ Book added successfully!")

    def remove_book(self):
        print("\n🗑️ Remove a Book:")
        title = input("Enter the title of the book to remove: ").strip().lower()
        removed = False

        for book in self.books:
            if book["title"].lower() == title:
                self.books.remove(book)
                removed = True
                print("✅ Book removed successfully.")
                break

        if not removed:
            print("❌ Book not found.")
        self.save_library()

    def search_books(self):
        print("\n🔍 Search for a Book:")
        keyword = input("Enter title or author: ").strip().lower()
        results = [book for book in self.books if keyword in book["title"].lower() or keyword in book["author"].lower()]
        if results:
            print(f"\nFound {len(results)} result(s):")
            self.display_books(results)
        else:
            print("❌ No matching books found.")

    def display_books(self, books=None):
        if books is None:
            books = self.books

        if not books:
            print("\n📚 No books to display.")
            return

        print("\n📚 Library Collection:")
        for i, book in enumerate(books, 1):
            read_status = "Read ✅" if book["read"] else "Unread ❌"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} [{read_status}]")
        print()

    def display_stats(self):
        print("\n📊 Library Statistics:")
        total = len(self.books)
        if total == 0:
            print("No books in your library.")
            return

        read_count = sum(1 for book in self.books if book["read"])
        percent_read = (read_count / total) * 100
        print(f"Total books: {total}")
        print(f"Books read: {read_count}")
        print(f"Percentage read: {percent_read:.1f}%")

    def menu(self):
        while True:
            print("\n==== 📚 Personal Library Menu ====")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_stats()
            elif choice == "6":
                print("👋 Exiting... Your library has been saved.")
                break
            else:
                print("❌ Invalid input. Please choose between 1 and 6.")


if __name__ == "__main__":
    manager = LibraryManager()
    manager.menu()
