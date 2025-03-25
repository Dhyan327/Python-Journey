# In this part I will learn about "Map, Filter and  Reduce Function"

"""The map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence.
   These functions are known as higher-order functions, as they take other functions as arguments."""


"""Map Function :~~>"""
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# Syntax :~~>
'''map(function, iterable)'''
# The function argument is a function that is applied to each element in the iterable argument.
# The iterable argument can be a list, tuple, or any other iterable object.

L = [1,2,3,4,5,6,7]
print(L)
print()

# Examples :~~>

def square(x):
    return x*x
# Now, if we want a new list that has the square of all the items of "L" then there are two ways :~~> (1) By for loop   (2) By map function
"""L1 = []
for i in L:
    L1.append(square(i))
print(L1) """

newl = list(map(square,L))
L1 = map(lambda x : x*x, L)                 # Using Lambda function with map function
print(newl)
print(list(L1))
print()


"""Filter Function :~~>"""
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.
# Syntax :~~>
'''filter(predicate, iterable)'''
# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. 
# The iterable argument can be a list, tuple, or any other iterable object.

# Examples :~~>

def filter_function(a):
    return a > 2
newl1 = list(filter(filter_function, L))
L2 = filter(lambda a : a>2, L)              # Using Lambda function with filter function
print(newl1)
print(list(L2))
print()


"""Reduce Function :~~>"""
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python.
# Syntax :~~>
'''reduce(function, iterable)'''
# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on.
# The reduce function returns the final result.
# It is important to note that the reduce function requires the functools module to be imported in order to use it.

# Examples :~~>

from functools import reduce

def mysum(x,y):
    return x + y
newl2 = reduce(mysum,L)

numbers = [1, 2, 3, 4, 5]
L3 = reduce(lambda x, y : x + y, numbers)
print(newl2)
print(L3)