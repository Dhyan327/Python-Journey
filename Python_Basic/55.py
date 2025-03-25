# In this part I will learn about "Inheritance" in python

""" When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class.
    In addition, it can have its own properties and methods, this is called as Inheritance. """

# Syntax :~~> (Inheritance)
"""
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class   """
# Here, Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

class Employee: 
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the Employee with ID {self.id} is : {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default and compulsory language is Python, which must be known!")

e1 = Employee("Dhyan",7)
e1.showDetails()
# e1.showlanguage()         # Here, it will raise error because "Employee" class has no function named "showLanguage()"

e2 = Programmer("Krunal",9)
e2.showDetails()
e2.showlanguage()

"""Types of inheritance :~~~>"""
#  1) Single Inheritance
#  2) Multiple Inheritance
#  3) Multilevel Inheritance
#  4) Hierarchical Inheritance
#  5) Hybrid Inheritance