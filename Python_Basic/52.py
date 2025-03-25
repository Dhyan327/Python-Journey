# In this part I will learn about "Constructors" in Oython.

""" A constructor is a special method in a class used to create and initialize an object of a class.
    Constructor is invoked(called) automatically when an object of a class is created."""

# A constructor is a unique function that gets called automatically when an object is created of a class.
# The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Syntax :~~>
def __init__(self):     # init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.
	# initializations
    pass

# Types of Constructors :~~>
""" 1) Parameterized Constructor
    2) Default Constructor """

"""Parameterized Constructor :~~~>"""
# When the constructor accepts arguments along with self, it is known as parameterized constructor.
# These arguments can be used inside the class to assign the values to the data members.

# Examples :~~>
class Person:

    def __init__(self, name, age, occ):
        self.name = name
        self.occupation = occ
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} years old and is a {self.occupation}")

a = Person("Dhyan",17,"Diploma Student")
b = Person("Krunal",20,"Degree Student")

a.info()
b.info()

print()


"""Default Constructor :~~~>"""
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

# Examples :~~>

class Details:
  def __init__(self):
    print("This is an Example of Default Constructor!")
c = Details()