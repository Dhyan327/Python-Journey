# In this part I will learn about "dir(), __dict__() and help() methods" in Python

""" We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code.
    In Python, there are three built-in functions that are commonly used to get information about objects: dir(), __dict__(), and help(). Let's take a look at each of them: """

# 1) The "dir()" Method :~~> 
""" The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. 
    It is a useful tool for discovering what you can do with an object. Example :--> """

class Employee:
    def __init__(self, emp_name, emp_id):
        self.name = emp_name
        self.id = emp_id

e = Employee("Dhyan","27")
print(dir(e))
print(e.__class__)
print()

# 2) The "__dict__()" Attribute :~~>
""" The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. Example :--> """   

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.version = "2.O"

p = Person("Dhyan",17,"Diploma Student")
print(p.__dict__)
print()

# 3) The "help()" Method :~~>
""" The help() function is used to get help documentation for an object, including a description of its attributes and methods. Example :--> """

help(e)     # Here, "e" is an object of class "Employee"

# Conclusion :~~>
""" In conclusion, dir(), __dict__(), and help() are useful built-in functions in Python that can be used to get information about objects. They are valuable tools for introspection and discovery. """