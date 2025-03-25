# In this part I will learn about "Raising Custom Errors" in python.

# In python, we can raise custom errors by using the raise keyword.

# Examples :~~>
a = int(input("Enter any value between 3 and 10 :"))

if(a<3  or a>10):
  raise  ValueError("Value should be between 5 and 9")

# Quick Quiz :~~>
# Write a program which accepts the input(In string) from user and raises the error if the input is not the "quit" word.

b = int(input("Enter a word :"))

if b != "quit":
  raise TypeError("Invalid input!!")


# However, sometimes we may need to create our own custom exceptions that serve our purpose.

# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

"""Syntax :~~>
class CustomError(Exception):
    code ...
try:
    code ...
except CustomError:
    code..."""

# This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.