# In this part I will learn about "Method Overriding"

# In Python, method overriding is a way to customize the behavior of a class based on its specific needs.
""" Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. 
    The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, 
    the version of the method in the derived class is executed, rather than the version in the base class. """

# Example :~~>

class Shape:
  def __init__(self, length, breath):
    self.length = length
    self.breath = breath
    
  def area(self):
      return self.length * self.breath

class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()
      
rec = Shape(7, 3)
print(f"Area of Rectangle with length {rec.length} and breath {rec.breath} is {rec.area()}")
cir = Circle(7)
print(f"Area of Circle with radius {cir.radius} is {cir.area()}")
print()

# Example :~~>

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):                 # Base salary calculation (generic)
        return self.base_salary

class FullTimeEmployee(Employee):                 # Derived class for full-time employees
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus    # Full-time employees get a base salary plus a bonus

class PartTimeEmployee(Employee):               # Derived class for part-time employees
    def __init__(self, name, base_salary, hours_worked, hourly_rate):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate         # Part-time employees get paid based on the hours they worked

class Intern(Employee):						# Derived class for interns
    def __init__(self, name, base_salary, stipend):
        super().__init__(name, base_salary)
        self.stipend = stipend

    def calculate_salary(self):
        return self.base_salary + self.stipend				# Interns get a base salary plus a fixed stipend

full_time_emp = FullTimeEmployee("Krunal", 50000, 10000)
part_time_emp = PartTimeEmployee("Om", 0, 100, 50)
intern = Intern("Dhyan", 2700, 300)

print(f"{full_time_emp.name}'s Salary : ${full_time_emp.calculate_salary()}")  		# Output: Krunal's Salary: $60000
print(f"{part_time_emp.name}'s Salary : ${part_time_emp.calculate_salary()}")   	# Output: Om's Salary: $5000
print(f"{intern.name}'s Salary : ${intern.calculate_salary()}")               		# Output: Dhyan's Salary: $3000


""" It's important to note that when you override a method, the new implementation must have the same method signature as the original method.
    This means that the number and type of arguments, as well as the return type, must be the same. """

# Conclusion :~~>
""" In conclusion, method overriding is a powerful feature in Python that allows you to customize the behavior of a class based on its specific needs. 
    By using method overriding, you can create more robust and reliable code, and ensure that your classes behave in the way that you need them to. 
    Additionally, by using the super function, you can extend the behavior of a base class method, rather than replace it, giving you even greater flexibility and control over the behavior of your classes. """