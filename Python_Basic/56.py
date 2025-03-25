# In this part I will learn about "Access Specifiers/Modifiers" in Python

# Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

"""Types of Access Specifiers"""

# 1)  Public access modifier
# 2)  Private access modifier
# 3)  Protected access modifier

""" 1) Public access modifier :~~>"""

# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

class Student:
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(17,"Dhyan")
print(obj.age)
print(obj.name)
print()

""" 2) Private Access Modifier :~~>"""

# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.
""" In Python, there is no strict concept of "private" access modifiers like in some other programming languages.
    However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). 
    This is known as a "weak internal use indicator" and it is a convention only, not a strict rule.
    Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified. """

class  Employee:
    def __init__(self,name,id,occ):
        self.__name = name                # An indication of private variable
        self.__id = id 
        self.__occupation = occ

    def __intro(self):                  # An indication of private Function 
        print(f"{self.__name} is a {self.__occupation} and his id number is {self.__id}")

obj1 = Employee("Dhyan",3,"Diploma Student")
# obj1.__intro()          # Here, if we try to execute the "__intro" method of class "Employee" then it will raise error that "__intro" attribute is not declared in the class "Employee" 

""" Private members of a class cannot be accessed or inherited outside of class.
    If we try to access or to inherit the properties of private members to child class (derived class),Then it will show the error. """

# Name Mangling :~~>
""" Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. 
    Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.  """
obj1._Employee__intro()   # Hence, Private members of a class cannot be accessed directly, but can be accessed indirectly through "Name Mangling".
print()

"""3) Protected Access Modifier :~~>"""

#  In OOP, the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses.
""" In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_).
    For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.  """
""" It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. 
    The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.  """

class Myself:
    def __init__(self):
        self._name = "Dhyan"
    
    def _welcome(self):
        return f"Hey, you are welcome from Dhyan"

class temporary(Myself):
    pass

obj2 = Myself()
print(obj2._name)
print(obj2._welcome())

obj3 = temporary()
print(obj3._name)
print(obj3._welcome())