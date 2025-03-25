# In this part I will learn about "How to use Class Methods as Alternative Constructor"

""" In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class.
    The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use. """

""" However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor.
    This is where class methods can be used as alternative constructors. """

""" A class method belongs to the class rather than to an instance of the class. One common use case for class methods is as alternative constructors. 
    When you want to create an object from data that is stored in a different format, such as a string or a dictionary."""

# For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like this:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
            
# But what if you want to create a Person object from a string that contains the person's name and age, separated by a comma? You can define a class method named "from_str" to do this:
    @classmethod
    def from_str(cls, string):
        name = string.split('-')[0]
        age = int(string.split('-')[1])
        return cls(name, int(age))

string = "Maniyar Dhyan - 17"
person = Person.from_str(string)
print("Name : ",person.name)
print("Age : ",person.age)
print()


class Employee:
    def __init__(self, emp_name, emp_id):
        self.name = emp_name 
        self.id = emp_id
    
    @classmethod
    def from_list(cls, lst):
        name = lst[0]
        id = int(lst[1])
        return cls(name, id)
    
lst = ["Maniyar Dhyan", 27]
employee  = Employee.from_list(lst)
print("Employee Name : ", employee.name)
print("Employee ID : ", employee.id)    