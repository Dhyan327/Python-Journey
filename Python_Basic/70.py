# In this part I will learn about "Hierarchical Inheritance"

""" Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. 
    In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner. """

# Example :~~>
class Employee:
    def __init__(self, name, age, employee_id, department):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.department = department
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}"

class Manager(Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size
    def get_details(self):
        return f"Manager - {super().get_details()}, Team Size: {self.team_size}"

class Developer(Employee):
    def __init__(self, name, age, employee_id, department, programming_languages):
        super().__init__(name, age, employee_id, department)
        self.programming_languages = programming_languages
    def get_details(self):
        return f"Developer - {super().get_details()}, Programming Languages: {', '.join(self.programming_languages)}"

class Designer(Employee):
    def __init__(self, name, age, employee_id, department, design_tools):
        super().__init__(name, age, employee_id, department)
        self.design_tools = design_tools
    def get_details(self):
        return f"Designer - {super().get_details()}, Design Tools: {', '.join(self.design_tools)}"

manager = Manager("Vishwa", 23, "M123", "Management", 10)
developer = Developer("Dhyan", 18, "D273", "IT", ["Python", "Java"])
designer = Designer("Charlie", 28, "DE789", "Creative", ["Photoshop", "Illustrator"])

print(manager.get_details())        # Output: Manager - Name: Vishwa, Age: 23, Employee ID: M123, Department: Management, Team Size: 10
print(developer.get_details())      # Output: Developer - Name: Dhyan, Age: 30, Employee ID: D456, Department: IT, Programming Languages: Python, Java
print(designer.get_details())       # Output: Designer - Name: Charlie, Age: 28, Employee ID: DE789, Department: Creative, Design Tools: Photoshop, Illustrator

# Conclusion :~~>
""" In conclusion, hierarchical inheritance is a way of establishing relationships between classes in a hierarchical manner. 
    It allows multiple subclasses to inherit from a single base class, which helps in code reuse and organization of code in a more structured manner. """