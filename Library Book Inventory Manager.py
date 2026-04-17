class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book Added")

    def search_book(self):
        name = input("Enter Title or Author: ")

        for book in self.books:
            if book.title == name or book.author == name:
                print(book.book_id, book.title, book.author, book.issued)

    def issue_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                book.issued = True
                print("Book Issued")

    def return_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                book.issued = False
                print("Book Returned")

    def report(self):
        total = len(self.books)
        issued = 0

        for book in self.books:
            if book.issued == True:
                issued += 1

        print("Total Books =", total)
        print("Issued Books =", issued)


lib = Library()

while True:
    print("\n1.Add Book")
    print("2.Search Book")
    print("3.Issue Book")
    print("4.Return Book")
    print("5.Report")
    print("6.Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        lib.add_book()

    elif ch == "2":
        lib.search_book()

    elif ch == "3":
        lib.issue_book()

    elif ch == "4":
        lib.return_book()

    elif ch == "5":
        lib.report()

    elif ch == "6":
        break

    else:
        print("Invalid Choice")