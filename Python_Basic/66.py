# In this part I will learn about "Single Inheritance"

# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

# Syntax :~~>
""" The syntax for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class definition, inside the parentheses, like this: 

class ChildClass(ParentClass):
    # class body   
"""

# Example :~~>
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def read(self):
        return f"Reading {self.title} by {self.author}."
    def book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

class Ebook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size
        self.current_page = 0

    def download(self):
        return f"Downloading {self.title} with a file size of {self.file_size} MB."

    def go_to_page(self, page):
        if 0 <= page < self.pages:
            self.current_page = page
            return f"Going to page {self.current_page} of {self.title}."
        else:
            return f"Invalid page number. {self.title} has {self.pages} pages."

    def ebook_info(self):
        base_info = self.book_info()
        return f"{base_info}, File Size: {self.file_size} MB"

my_ebook = Ebook("2007", "Jainism World", 327, 1.5)

print(my_ebook.download())              # Output: Downloading 2007 with a file size of 1.5 MB.
print(my_ebook.read())                  # Output: Reading 2007 by Jainism World.
print(my_ebook.go_to_page(50))          # Output: Going to page 50 of 2007.
print(my_ebook.ebook_info())            # Output: Title: 2007, Author: Jainism World, Pages: 327, File Size: 1.5 MB
print(my_ebook.go_to_page(400))         # Output: Invalid page number. 2007 has 327 pages.
print()

# Example :~~>
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, My Name is {self.name}, \nAnd I am {self.age} years old."
    
class Employee(Person):
    def __init__(self, name, age, employee_id, position) -> None:
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position
    
    def employee_info(self):
        return f"Employee ID: {self.employee_id} \nPosition: {self.position}"

emp = Employee("Dhyan", 17, "E327", "Python Developer")
print(emp.greet())
print(emp.employee_info())

# Conclusion :~~>
""" Single inheritance is a powerful tool in Python that allows you to create new classes based on existing classes. 
    It allows you to reuse code, extend it to fit your needs, and make it easier to manage complex systems.
    Understanding single inheritance is an important step in becoming proficient in object-oriented programming in Python. """