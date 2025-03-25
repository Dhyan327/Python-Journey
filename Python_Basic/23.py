# In this part I will learn about "Variable- Length Argument and Return Statement"
# Variable- Length Arguments :-->
""" 
Sometimes we may need to pass more arguments than those defined in the actual function. 
This can be done using Variable- Length Arguments.
There are two ways to achieve this :-
1 ~~> Arbitary Arguments 
2 ~~> Keyword Arbitary Arguments
"""
# [1] ~ Arbitary Arguments :-->
# While creating a function pass (*) symbol before the parameter name while definning the function. The Function access the arguments by processing them in the form of "Tuple"
# Example :--> [Arbitary Arguments]
def average(*numbers):
    print(type(numbers))      # Here, The "numbers" is taken as "Tuple Datatype"
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The Average is", sum/len(numbers))
average(8, 7, 6, 5)
# Example given in Tutorial
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("Maniyar", "Dhyan", "Hemantbhai")
print("\n")

# [2] ~ Keyword Arbitary Arguments :-->
# While creating a function pass (**) before the parameter name while the function. The function accesses the argument by processing them in the form of "Dictionary"                                                   
# Example :--> [Keyword Arbitary Arguments]
def name1(**name):
    print(type(name))       # Here, The "name" is taken as "Dictionary Datatype" 
    print("Hello,", name["fname"], name["mname"], name["lname"])
name1(mname = "Dhayn", lname = "Hemantbhai", fname = "Maniyar")

# Return Statement :-->
# The return statement is used to return the value of the expression back to the calling function  
def average1(*num):
    sum = 0
    for i in num:
        sum = sum + i
    # return 7                # If we write two return statement then the first statement will be executed  
    return sum / len(num)
x = average1(8, 7, 6, 5)
print("The Average is",x)

def name2(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name2("Maniyar", "Dhyan", "Hemantbhai"))