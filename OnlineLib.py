class Library:
    def __init__(self, list_of_books, Lib_name):
        self.list_of_books = list_of_books
        self.Li_Name = Lib_name
        self.lend_dict = {}

    def display_book(self):
        for item in self.list_of_books:
            print(item)

    def lend_book(self, name, book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book: name})
            print("Book lended")
        else:
            print("Book not available")

    def add_book(self, book):
        self.list_of_books.append(book)
        print("Book has been added")

    def ret_book(self, item):
        self.lend_dict.pop(item)
        print("Book Returned")


if __name__ == '__main__':
    parag = Library(['Harry Potter', 'Nagraj', 'Dhruva', 'Batman', 'Python', 'Sixteen'], "Meri Library")

while True:
    print(f"Welcome to Online Library named Meri Library:", "Enter your choice")
    print("1. Display Books")
    print("2. Lend Books")
    print("3. Add Books")
    print("4. Return Books")
    print("5. List of Lended Books")

    x = int(input())
    if x == 1:
        print("Collection Of Books in Our Library\n")
        parag.display_book()
    elif x == 2:
        book = input("Enter the book you want to lend?")
        name = input("Enter Your Name Please")
        parag.lend_book(name, book)
    elif x == 3:
        y = input("Which book you want to add?")
        parag.add_book(y)
    elif x == 4:
        z = input("Which book you want to return?")
        parag.ret_book(z)
    elif x == 5:
        print(parag.lend_dict)
    else:
        print("Invalid Input")

