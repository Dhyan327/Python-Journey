# In this part I will learn about "Classes and Objects in Python"

""" A class is a blueprint or a template for creating objects,
    providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
    The user-defined objects are created using the class keyword."""

# Let us now create a class using the class keyword.

class Person:
    name = "Dhyan"
    age  = 17
    occupation = "Diploma Student"

    def info(self):                                         # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        return (f"{self.name} is an {self.occupation}")     # It must be provided as the extra parameter inside the method definition.

    
# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
  
obj1 = Person()
print(obj1)
print(type(obj1))

print()

print(obj1.name)
print(obj1.age)
print(obj1.occupation)
print(obj1.info())

print()

obj2 = Person()
obj2.name = "Krunal"
obj2.age = 20
obj2.occupation = "Degree Student"
print(obj2.name)
print(obj2.age)
print(obj2.occupation)
print(obj2.info())