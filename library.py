class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
        print(f"Confirmation: You have successfully borrowed '{self.title}' by {self.author}.")
    def return_book(self):
        self.is_borrowed = False
        print(f"Confirmation: You have successfully returned '{self.title}' by {self.author}.")
if __name__ == "__main__":
    print("---Initializing 3 book objects---")
    book_1 = Book("Around the Worls in 80 days","Jules Verne")
    book_2 = Book("Harry Potter", "JK Rowling")
    book_3 = Book("The Boy","Roald Dahl")

    print("\n--- Demonstrating borrow() method---")
    book_1.borrow()
    book_2.borrow()

    book_1.return_book()
    book_3.borrow()
    book_3.return_book()
