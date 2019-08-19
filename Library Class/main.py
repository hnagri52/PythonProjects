class Library():
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"There are the following books in {self.name}'s library: ")
        i = 1
        for book in self.booksList:
            print(str(i) + " " + book)
            i+=1
        print("\n")

    def lendBook(self, user, book):
        """Lending a book """
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("The book collection has been updated! You can take this book now")
        else:
            print(f"The book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("The booklist has been updated! ")


    def returnBook(self, book):
        self.lendDict.pop(book)


def main():
    Hussein = Library(["harrypotter1", "hp2", "hp3", "hp4"], "Hussein")


    while True:
        print(f"Welcome to the {Hussein.name} library! Enter a number to continue:")
        print("1. Display book")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        print("if you would like to exit, press q")
        user_choice = input()


        if int(user_choice) == 1:
            Hussein.displayBook()

        elif int(user_choice) == 2:
            book = input("Enter the book you want to lend")
            user = input("Enter your name!")

            Hussein.lendBook(book, user)

        elif int(user_choice) == 3:
            book = input("Enter the name of the book you want to add:")
            Hussein.addBook(book)

        elif int(user_choice) == 4:
            book = input("Enter the name of the book you want to return:")
            Hussein.returnBook(book)

        elif user_choice == "q":
            break

        else:
            print("Not a valid option")


if __name__ == '__main__':
    main()
