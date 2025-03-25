# In this part I will learn about "Lambda Function"

# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:
# Syntax :~~>
"""lambda arguments: expression"""

# Lambda functions are often used in situations where a small function is required for a short period of time.
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

#  Examples :~~>

"""
def double(x):          #  Function to double the input
    return x * 2
"""

double = lambda x : x * 2           # Lambda function to double the input
cube = lambda x : x*x*x             # Lambda function to return the cube of the input
add = lambda x, y : x + y           # Lambda function to return the sum of the input
avg = lambda x, y, z : (x+y+z)/3    # Lambda function to return the average of the input

print(double(3))
print(cube(5))
print(add(3,7))
print(avg(3,5,7))

# Example of using function as an argument :~~>

def apply(function,value):
    return function(value)

# The above function can also be written in the form of lambda function
"""apply = lambda function, value : function(value)"""

square = lambda x : f"The Square of {x} is : {x*x}"

print(apply(square,7))
print(apply(lambda x : x*x, 10))