# In this part I will learn about "Difference of Instance variables and Class variables"

# In Python, variables can be defined at the class level or at the instance level.

# Class Variables :~~>
""" Class variables are defined at the class level and are shared among all instances of the class.
    They are defined outside of any method and are usually used to store information that is common to all instances of the class.
    For example, a class variable can be used to store the number of instances of a class that have been created. """

class MyClass:
    class_variable = 0          # Here, "Class_Variable" is an Class Variable
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print("Number of Instances : ",MyClass.class_variable)

""" In the example above, the class_variable is shared among all instances of the class MyClass.
    When we create new instances of MyClass, the value of class_variable is incremented.
    When we call the print_class_variable method on obj1 and obj2, we get the same value of class_variable. """

obj1 = MyClass()
obj1.print_class_variable()     # Output: 1
obj2 = MyClass()
obj2.print_class_variable()     # Output: 2
print()

# Instance Variables :~~>
""" Instance variables are defined at the instance level and are unique to each instance of the class.
    They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
    For example, an instance variable can be used to store the name of an employee in a class that represents an employee."""

class intro:
    def __init__(self,name):
        self.name = name            # Here, "name" from "self.name" is an instance variable

    def showDetails(self):
        print(f"Hello, My name is {self.name}")

# In the example above, each instance of the class intro has its own value for the name variable. When we call the showDetails method on obj3 and obj4, we get different values for name.

obj3 = intro("Dhyan")
obj3.showDetails()          
obj4 = intro("Krunal")
obj4.showDetails()

# Summary :~~>
""" In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances.
    Instance variables are unique to each instance of a class and are used to store information that is specific to each instance. """

""" It's also worth noting that, in python, class variables are defined outside of any methods and don't need to be explicitly declared as class variable.
    They are defined in the class level and can be accessed via classname.varibale_name or self.class.variable_name.
    But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name. """