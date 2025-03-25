# In this part I will do "Exercise 6 Solution"
# Exercise :->
''' Write a Library class with "no_of_books" and "books" as two instance variables.
    Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods.
    Show that your program doesnt persist the books after the program is stopped!
'''

# Solution :~~>
class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def addBook(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def showInfo(self):
        print(f"The Library has {self.no_of_books} books. The Books are :-")
        for index,i in enumerate(self.books, start=1):
            print(f"{index} : {i}")

l1 = Library()
l1.addBook("Rich Dad, Poor Dad")
l1.addBook("Ali Baba and the Forty Thieves")
l1.addBook("World of Jainism")
l1.showInfo()