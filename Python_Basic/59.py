# In this part I will learn about "Class Methods"

# Python Class Methods :~~>
""" A class method is a type of method that is bound to the class and not the instance of the class. 
    In other words, it operates on the class as a whole, rather than on a specific instance of the class. 
    Class methods are defined using the "@classmethod" decorator, followed by a function definition. 
    The first argument of the function is always "cls," which represents the class itself. """

# Class methods are useful in several situations.
""" For example, It is to provide alternative constructors for your class.
    This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so. """

""" To define a class method, you simply use the "@classmethod" decorator before the method definition.
    The first argument of the method should always be "cls," which represents the class itself. Here is an example :- """

class Employee:
    company = "Microsoft"
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name is {self.name} and his Company is {self.company}")
    
    @classmethod
    def changeCompany(cls, newcompany):     # Here, Instead of "cls" we can also write "self" or any other word such as "phy" etc..
        cls.company = newcompany        

# Note :-->
""" In this function, if we not include "@classmethod" decorator, then this function will only change the value of variable "company" for the particular instance only.
    So, if we wanted to change the value of variable at class level, then we must include "@classmethod" decorator before the definition of that function """

e1 = Employee("Dhyan")
e2 = Employee("Krunal")

e1.show()
print(f"Company name is {Employee.company}")
e1.changeCompany("Google")
print()

e2.show()
print(f"Company name is {Employee.company}")

# Conclusion :~~>
""" Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. 
    They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. """