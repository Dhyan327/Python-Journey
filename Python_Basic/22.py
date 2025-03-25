# In this part I will learn about "Function Argument"
"""
There are four types of argument that we can provide in a function :-->
1 ~~> Default Arguments
2 ~~> Keyword Arguments
3 ~~> Variable Length Arguments
4 ~~> Required Arguments
"""
# Default Argument :-->
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

# Examples :--> [Default Arguments]
def average(a=7,b=3):
    print("The average is", (a+b)/2)
average()       # Now, The interpreter will give the average of the default value given with the function as output
average(27,3)   # Here, The interpreter will the average of 27 and 3 as output irrespective of the default value
average(5)      # If we only give the value of 'A(Eg-5)' then the value of 'B' will be taken as Default value given in the function i.e. "3"
average(b=5)    # If we only give the Value of 'B(Eg-5)' then the value of 'A' will be taken as Default value given in the function i.e. "7"

# Example given in the tutorial :-->
def name(fname, mname="Hemantbhai", lname="Maniyar"):
    print("Hello", fname, mname, lname)
name("Dhyan")
print("\n")

# Keyword Arguments :--> [Keyword Arguments]
# We can provide Argument with "Key = value", this way the interpreter recognizes the argument by the parameter name. Hence, The order in which the argument passed does not matter
# Example :-->
average(b=3, a=7)  
name(lname="Hemantbhai", fname="Maniyar", mname="Dhyan")
print("\n")

# Required Arguments :--> [Required Argument]
''' In case we don't pass the arguments with a "Key = value" syntax,
 Then it is necessary to pass the arguments in the correct possitional order and the number of arguments should match with the actual function definition.'''
# Example :--> [Required Arguments]
def name1(F_name, M_name, L_name):
    print("Hello", F_name, M_name, L_name)
name1("Maniyar","Dhyan", "Hemantbhai")     # If we will not write any one of the value then it will give Error as output
print("\n") 