# In this part I will learn about "Multiple Inheritance"

""" Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. 
    This can be useful in situations where a class needs to inherit functionality from multiple sources. """

# Syntax :~~>
""" In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.

class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body  
"""
# Example :~~>

class Developer:
    def __init__(self, programming_language):
        self.programming_language = programming_language
    def write_code(self):
        print(f"Writing code in {self.programming_language}.")

class Designer:
    def __init__(self, tool):
        self.tool = tool
    def create_design(self):
        print(f"Creating design using {self.tool}.")

class HybridEmployee(Developer, Designer):              # Defining the child class inheriting from both Developer and Designer class
    def __init__(self, programming_language, tool):
        Developer.__init__(self, programming_language)
        Designer.__init__(self, tool)
    def perform_tasks(self):
        self.write_code()
        self.create_design()

emp1 = HybridEmployee("Python", "Photoshop")
emp1.perform_tasks()
print()

# Note :~~>
""" It's important to note that, in case of multiple inheritance, 
    Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. 
    The MRO determines the order in which parent classes are searched for attributes and methods. """

# Example :~~>

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Developer:
  def __init__(self, lang):
    self.lang = lang
  def show(self):
    print(f"Writing Code in {self.lang}")

class DeveloperEmployee(Employee, Developer):       # Here, if we alter the order of the parent classes then "Developer.mro()" will be changed,
  def __init__(self, name, lang):                   # Hence, the output of emp2.show() will also change
    self.name = name
    self.lang = lang

emp2 = DeveloperEmployee("Dhyan","Python")
emp2.show()
print(DeveloperEmployee.mro())