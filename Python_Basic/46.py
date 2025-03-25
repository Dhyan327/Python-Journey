# In this part I will learn about Local and Global variable in python

"""Local Variable :~~>"""
# A local variable is a variable that is defined within a function and is only accessible within that function.
# It is created when the function is called and is destroyed when the function returns.

"""Global Variable :~~>"""
# A global variable is a variable that is defined outside of any function and can be accessed and modified from anywhere within the code.
# This means that the variable is available for use in all parts of the code, including inside functions.

# Example :-->
x = 10          # global variable

def my_function():
  x = 5         # local variable
  print(f"The Local x is {x}")

my_function()
print(f'The Global x is {x}')

"""Global Keyword :~~>"""
# The global keyword in Python is used to tell the program that a variable defined inside a function should be treated as a global variable, allowing the function to modify its value

a = 10          # global variable

def my_function1():
  global a
  a = 5         # this will change the value of the global variable x
  b = 5         # local variable

my_function1()
print(a)        # prints 5
# print(b)      This will cause an error because y is a local variable and is not accessible outside of the function