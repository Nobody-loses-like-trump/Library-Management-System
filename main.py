class Library:
    books = ["Harry Potter 1", "Harry Potter 2", "Harry Potter 3"]

    def __init__(self):
        self.books = []

    @classmethod
    def display_books(cls):
        for index, value in enumerate(cls.books):
            print(f"{index + 1}) {value}")

    def lend_book(self, index):
        book = Library.books[index - 1]
        self.books.append(book)
        Library.books.remove(book)

    @classmethod
    def add_book(cls, book):
        cls.books.append(book)

    def return_book(self, index):
        book = self.books[index - 1]
        self.books.remove(book)
        Library.books.append(book)

    def display_self_books(self):
        for index, value in enumerate(self.books):
            print(f"{index + 1}) {value}")


user = Library()
while 1:
    while 1:
        print("Press 1 to display available books")
        print("Press 2 to lend a book")
        print("Press 3 to donate a book")
        print("Press 4 to return a lent book")
        print("Press 5 to display lent books")

        choice = input()

        if choice in ["1", "2", "3", "4", "5"]:
            choice = int(choice)
            break
        else:
            print("Invalid input it must be in [1, 2, 3, 4, 5]")

    if choice == 1:
        Library.display_books()
    elif choice == 2:
        if len(Library.books) == 0:
            print("There are no more books to lend")
        else:
            Library.display_books()
            while 1:
                print("Press 99 to break")
                book_index = input("Which book do you want to lend (Enter the index)")
                if book_index == "99":
                    break

                try:
                    book_index = int(book_index)
                    if book_index not in range(1, len(Library.books) + 1):
                        print("Invalid input it must be a index of a book")
                    else:
                        user.lend_book(book_index)
                        break
                except ValueError:
                    print("Invalid input it must be a index of a book")
    elif choice == 3:
        while 1:
            print("Press 99 to break")
            book_donate = input("Enter the name of the book you want to donate")
            if book_donate == "99":
                break

            if book_donate not in Library.books:
                Library.add_book(book_donate)
                break
            else:
                print("Book already in Library")
    elif choice == 4:
        if len(user.books) == 0:
            print("You don't have any books to return")
        else:
            user.display_self_books()
            while 1:
                print("Press 99 to break")
                book_index = input("Which book do you want to lend (Enter the index)")
                if book_index == "99":
                    break
                try:
                    book_index = int(book_index)

                    if book_index not in range(1, len(user.books) + 1):
                        print("Invalid input it must be a index of a book")
                    else:
                        user.return_book(book_index)
                        break
                except ValueError:
                    print("Invalid input it must be a index of a book")
    elif choice == 5:
        user.display_self_books()
    print()
