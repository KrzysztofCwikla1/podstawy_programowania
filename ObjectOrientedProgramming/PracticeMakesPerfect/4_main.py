# ebook.py
class Ebook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.is_open = False

    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def next_page(self):
        if self.is_open and self.current_page < self.pages:
            self.current_page += 1
        elif not self.is_open:
            print("The book is closed.")

    def previous_page(self):
        if self.is_open and self.current_page > 0:
            self.current_page -= 1
        elif not self.is_open:
            print("The book is closed.")

    def status(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")
        print(f"Pages: {self.pages}, Current Page: {self.current_page}")
        print("Status: Open" if self.is_open else "Status: Closed")

def main():
    book = Ebook("The Great Gatsby", "F. Scott Fitzgerald", 180)

    print("Book status:")
    book.status()

    print("\nOpen the book:")
    book.open_book()
    book.status()

    print("\nRead a few pages:")
    for _ in range(5):
        book.next_page()
    book.status()

    print("\nClose the book and try to read:")
    book.close_book()
    book.next_page()
    book.previous_page()

if __name__ == "__main__":
    main()

