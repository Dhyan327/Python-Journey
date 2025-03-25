# In this part I will learn about "Exception Handling in python"

# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. 
"""Exception handling deals with these events to avoid the program or system crashing,
 and without this process, exceptions would disrupt the normal operation of a program."""

# try...except blocks are used in python to handle errors and exceptions.
"""The code in try block runs when there is no error.
   If the try block catches the error, then the except block is executed.
"""

# Syntax :~~>
"""
try:
    statements which could generate 
    exception
except:
    Soloution of generated exception"""

# Examples :~~>
a = input("Enter the Number :")
print(f"Multiplication table of {a} is :")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("\n")

# Example given in Tutorial :-->
try:
    a = [3,7,10,13,17,27,30]
    print(a)
    num = int(input("Enter an index: "))
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

print("End of the program!!!")
print("Copyright @ Dhyan")