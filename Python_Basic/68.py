# In this part I will learn about "Multi-level Inheritance"

""" Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. 
    This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class. """

# Syntax :~~>
""" In Python, The syntax for multilevel inheritance is quite simple and follows the same syntax as single inheritance.

class BaseClass:
    # Base class code
    
class DerivedClass1(BaseClass):
    # Derived class 1 code
    
class DerivedClass2(DerivedClass1):
    # Derived class 2 code
"""

# Example :~~>
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")

class SeniorDeveloper(Developer):
    def __init__(self, name, salary, programming_language, experience):
        Developer.__init__(self, name, salary, programming_language)
        self.experience = experience

    def lead_project(self):
        print(f"{self.name} with {self.experience} years of experience is leading the project.")

senior_dev = SeniorDeveloper("Dhyan", 120000, "Python", 7)

senior_dev.show_details()       # Output: Name: Dhyan, Salary: $120000
senior_dev.write_code()         # Output: Dhyan is writing code in Python.
senior_dev.lead_project()       # Output: Dhyan with 7 years of experience is leading the project.
print()

# Example :~~>
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

obj = GoldenRetriever("Tommy", "Black")
obj.show_details()
print(GoldenRetriever.mro())

""" Another important aspect of multilevel inheritance is that it allows you to reuse code and avoid repeating the same logic multiple times. 
    This can lead to better maintainability and readability of your code, as you can abstract away complex logic into base classes and build upon them. """

# Conclusion :~~>
"""  In conclusion, multilevel inheritance is a powerful feature in object-oriented programming that allows you to create complex and intricate classes by building upon existing ones. 
    It provides the benefits of code reuse, maintainability, and readability, while also requiring careful consideration to avoid potential problems. """