# In this part I will learn about "Magic(Dunder) Method"

""" Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. 
    They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties. """

# These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

""" Lets take a look at some of the most commonly used magic methods in Python. """

# 1) "__init__" Method :~~>
""" The init method is a special method that is automatically invoked when you create a new instance of a class. It is also referred as "constructor"
    This method is responsible for setting up the objects initial state, and it is where you would typically define any instance variables that you need. """

# 2) "__str__" and "__repr__" Method :~~>
""" The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, 
    while the repr method is used when you want to get a string representation of an object that can be used to recreate the object. """

# 3) "__len__" Method :~~>
""" The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary. """

# 4) "__call__" Method :~~>
""" The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called.
    This is an incredibly powerful tool that allows you to create objects that behave like functions. """

# Example :~~>

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.id}")
    def __len__(self):
        length = 0
        for i in self.name:
            length = length + 1
        return length
    def __str__(self):
        return f"Employee ID {self.id} - Employee Name {self.name}  --> from __str__"
    def __repr__(self):
        return f"Employee ID {self.id} - Employee Name {self.name}  --> from __repr__"
    def __call__(self):
        print("Employee is called")
    
Dhyan = Employee("Dhyan",7)
Dhyan.show()
print()
print(f"Length of {Dhyan.name} is {len(Dhyan)}")     # Here, if the class Employee has no method named "__len__" then it raise an error
print(Dhyan)                                         # Here, if the class Employee has no method name "__str__" or "__repr__" then it will give output as an object address
print(str(Dhyan))       # Use case for __str__ method
print(repr(Dhyan))      # Use case for __repr__ method
Dhyan()                 # Here, if the class Employee has no method named "__call__" then it raise an error

# Conclusion :~~~>
""" In Conclusion, These are just a few of the many magic methods available in Python. 
    They are incredibly powerful tools that allow you to customize the behaviour of your objects, and can make your code much cleaner and easier to understand.
    So if you are looking for a way to take your Python code to the next level, take some time to learn about these magic methods. """