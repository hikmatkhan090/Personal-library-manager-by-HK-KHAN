import os
import random

# 🌟 Motivational quotes to encourage reading
QUOTES = [
    "📖 A reader lives a thousand lives before he dies.",
    "🌱 Reading is to the mind what exercise is to the body.",
    "✨ Today a reader, tomorrow a leader.",
    "🧠 Knowledge is power. Read on!",
    "📚 Books are a uniquely portable magic."
]

LIBRARY_FILE = "library.txt"


def load_library():   # 📂 Load library from file
    library = []
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 6:
                    book_id, title, author, year, genre, read_status = parts
                    library.append({
                        "id": int(book_id),
                        "title": title,
                        "author": author,
                        "year": int(year),
                        "genre": genre,
                        "read_status": read_status == "True"
                    })
                else:
                    print(f"⚠️ Skipping malformed line: {line}")
    else:
        with open(LIBRARY_FILE, "w") as file:
            print("🆕 Created new library file.")
    return library

# 💾 Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        for book in library:
            file.write(f"{book['id']}|{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{book['read_status']}\n")

# ➕ Add a new book
def add_book(library):
    print("\n📘 Add New Book:")
    try:
        title = input("🔤 Title: ").strip()
        author = input("🖋️ Author: ").strip()
        year = int(input("📅 Year: "))
        genre = input("🎭 Genre: ").strip()
        read_status = input("✅ Read? (yes/no): ").strip().lower() == "yes"
        book_id = max([book["id"] for book in library], default=0) + 1
        library.append({
            "id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        })
        print("🎉 Book added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Please try again.\n")

# ➖ Remove a book by ID
def remove_book(library):
    try:
        book_id = int(input("🗑️ Enter Book ID to remove: "))
        for book in library:
            if book["id"] == book_id:
                library.remove(book)
                print("✅ Book removed.\n")
                return
        print("❌ Book ID not found.\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")

# 🔍 Search by title or author
def search_books(library):
    print("\n🔍 Search Options:")
    print("1. Title")
    print("2. Author")
    choice = input("Choose an option: ").strip()
    query = input("Enter search keyword: ").strip().lower()
    if choice == "1":
        matches = [b for b in library if query in b["title"].lower()]
    elif choice == "2":
        matches = [b for b in library if query in b["author"].lower()]
    else:
        print("⚠️ Invalid choice.\n")
        return
    display_books(matches)

# 📚 Display all or filtered books
def display_books(books):
    if not books:
        print("\n📭 No books to display.\n")
        return
    print("\n📚 Book List:")
    print("-" * 50)
    for book in books:
        status_icon = "✅" if book["read_status"] else "❌"
        print(f"ID: {book['id']} | {book['title']} by {book['author']} ({book['year']}) | {book['genre']} | {status_icon}")
    print("-" * 50)
    print(f"💡 {random.choice(QUOTES)}\n")

# 📊 Show reading stats
def show_statistics(library):
    total = len(library)
    read = sum(b["read_status"] for b in library)
    print(f"\n📊 Total: {total} books")
    print(f"✅ Read: {read} ({(read/total)*100:.1f}%)" if total > 0 else "⚠️ No books yet.")
    print()

# 🎯 Filter by genre or read status
def filter_books(library):
    print("\n🎯 Filter Options:")
    print("1. Genre")
    print("2. Read Status")
    choice = input("Select option: ").strip()
    if choice == "1":
        genre = input("Enter genre: ").strip().lower()
        matches = [b for b in library if genre == b["genre"].lower()]
        display_books(matches)
    elif choice == "2":
        status = input("Read or Unread? ").strip().lower()
        is_read = status == "read"
        matches = [b for b in library if b["read_status"] == is_read]
        display_books(matches)
    else:
        print("⚠️ Invalid filter option.\n")

# 🌟 Main app loop
def main():
    print("\n📚 Welcome to Advanced Personal Library Manager 📚\n")
    library = load_library()
    while True:
        print("📋 Menu")
        print("1. ➕ Add Book")
        print("2. ➖ Remove Book")
        print("3. 🔍 Search Book")
        print("4. 📚 View All Books")
        print("5. 📊 Statistics")
        print("6. 🎯 Filter Books")
        print("7. 💾 Save & Exit")
        choice = input("👉 Your choice: ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            show_statistics(library)
        elif choice == "6":
            filter_books(library)
        elif choice == "7":
            save_library(library)
            print("📁 Library saved. Goodbye! 👋\n")
            break
        else:
            print("⚠️ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
