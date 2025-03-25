# In this part I will learn about "How import works in python"

""" The import statement in Python allows you to access the functions and variables defined in a module from within your current script.
    You can import the entire module, specific functions or variables, or use the * wildcard to import everything."""

# To import a module in Python, you use the import statement followed by the name of the module.

# There are three ways of importing a module :
import math         # In this way, if we want to use the function of any module then we have write the module name followed by dot(.) and the function name. eg :- math.sqrt(9)
from math import *  # Here, there is no need to write the module name to use its function. eg :- sqrt(9)
import math as m    # Here, instead of writing the module name at the starting we have write the string written after "as"  keyword followed by dot(.) and the function name. eg :- m.sqrt(9)
from math import sqrt, pi       # we can also import multiple functions or variables at once by separating them with a comma:  

# Once a module is imported, you can use any of the functions and variables defined in the module.
result = math.sqrt(9)
print(result)           # If we use "import math" statement then this is to be followed.

print(factorial(5))     # If we use "from math import * " statement then this is to be followed.

res = pow(3,2)          # If we use "import math as m" statement then this is to be followed.
print(res) 
print("\n")

""" Python has a built-in function called "dir" that you can use to view the names of all the functions and variables defined in a module.
    This can be helpful for exploring and understanding the contents of a new module."""
print(dir(math))