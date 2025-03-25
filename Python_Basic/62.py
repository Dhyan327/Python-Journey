# In this part I will learn about "Super Keyword"

""" The super() keyword in Python is used to refer to the parent class. 
    It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes. """

""" When a class inherits from a parent class, it can override or extend the methods defined in the parent class. 
    However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy. """

# Example :~~>

class ParentClass:
    def Parent_Method(self):
        print("This is Parent Method from Parent Class!")
    def Class_Method(self):
        print("This is Child Method from Parent Class!")

class ChildClass(ParentClass):
    def Parent_Method(self):
        print("This is Parent Method from Child Class!")
        super().Parent_Method()                            # This will call the Parent_Method from ParentClass
    def Class_Method(self):
        print("This is Child Method from Child Class!")
        super().Class_Method()                             # This will call the Class_Method from ParentClass

child_obj = ChildClass()
child_obj.Parent_Method()
child_obj.Class_Method()
print()

# Example :~~>

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.id}")
    
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)          # Call the __init__ method of the parent class Employee to initialize name and id
        self.lang = lang

    def show(self):
        print(f"Name: {self.name}, ID: {self.id}, Language: {self.lang}")
        
Krunal = Employee("Krunal",2)
Dhyan = Programmer("Dhyan",7,"Python")
Krunal.show()
Dhyan.show()

# Conclusion :~~>
""" In conclusion, the super() keyword is a useful tool in Python when you want to call a parent class method in a child class. 
    It can be used in inheritance scenarios with a single parent class or multiple parent classes. """