# In this part I will learn about "Hybrid Inheritance"

""" Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. 
    It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, 
    and single inheritance is used to inherit the properties of the derived class into a sub-derived class. """

""" Hybrid Inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class. """

# Syntax :~~>
""" The syntax for implementing Hybrid Inheritance in Python is the same as for implementing Single Inheritance, Multiple Inheritance, or Hierarchical Inheritance.

Here's the syntax for defining a hybrid inheritance class hierarchy:

class BaseClass1:
  # attributes and methods

class BaseClass2:
  # attributes and methods

class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods
"""

# Example :~~>

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def display_employee_info(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        Employee.__init__(self, name, emp_id)
        self.programming_language = programming_language
    def display_developer_info(self):
        print(f"Programming Language: {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        Employee.__init__(self, name, emp_id)
        self.team_size = team_size
    def display_manager_info(self):
        print(f"Team Size: {self.team_size}")

class TeamLeader(Developer, Manager):
    def __init__(self, name, emp_id, programming_language, team_size, project_name):
        Developer.__init__(self, name, emp_id, programming_language)
        Manager.__init__(self, name, emp_id, team_size)
        self.project_name = project_name
    def display_team_leader_info(self):
        super().display_employee_info()
        super().display_developer_info()
        super().display_manager_info()
        print(f"Project Name: {self.project_name}")

t = TeamLeader("Dhyan", "TL1234", "Python", 7, "Jarvis AI Virtual Assistant")      
t.display_team_leader_info()     
print()

# Example :~~>

class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id
    def display_info(self):
        print(f"Name: {self.name}, Staff ID: {self.staff_id}")

class TeachingStaff(Staff):
    def __init__(self, name, staff_id, department):
        Staff.__init__(self, name, staff_id)
        self.department = department
    def display_department(self):
        print(f"Department: {self.department}")

class AdminStaff(Staff):
    def __init__(self, name, staff_id, role):
        Staff.__init__(self, name, staff_id)
        self.role = role
    def display_role(self):
        print(f"Role: {self.role}")

class FacultyAdmin(TeachingStaff, AdminStaff):
    def __init__(self, name, staff_id, department, role, office_location):
        TeachingStaff.__init__(self, name, staff_id, department)
        AdminStaff.__init__(self, name, staff_id, role)
        self.office_location = office_location
    def display_faculty_admin_info(self):
        super().display_info()
        super().display_department()
        super().display_role()
        print(f"Office Location: {self.office_location}")

faculty_admin = FacultyAdmin("Dhyan Maniyar", "FA2703", "Computer Science", "Principal", "Main Building, Room 201")
faculty_admin.display_faculty_admin_info()

# Conclusion :~~>
""" In Conclusion, Hybrid Inheritance allows for a flexible and powerful way to inherit attributes and behaviors from multiple classes in a hierarchy or chain. """