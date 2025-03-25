# In this part I will learn about "Docstrings In Python"
# In Python, both docstrings and comments are used to document code, but they serve different purposes. 

# Comments VS Docstrings :-->
# Comments :-
'''A comment is a line of text that is added to the code to explain what the code is doing
   Comments are ignored by the Python interpreter and are not executed.'''
# Docstrings :-
''' A docstring is a string literal that is used to document a module, function, class, or method.
 Docstrings are used to describe what the code does, provide usage examples, and explain any relevant details. '''
# We can access these docstrings using the doc attribute.

# Example given in Tutorial :-->
def square(n):
    '''Takes in a number n and returns the square of n'''
    print(n*n)
square(5)            
print(square.__doc__)       # square.__doc__  is used to access the docstring (documentation string) associated with the function  square()

print("\n")

# Note :- Python docstrings have to be written just right after the definition of a function, module etc, otherwise when we will access it, the python interpreter will return none                                     
# Example :-
def square1(i):
    print(i**2)
    '''Takes in a number n and returns the square of n'''
square1(3)
print(square1.__doc__)      # This will return "None" because here, Docstring is not written just after the definition of function

print("\n")

# Example :-
def add(num1, num2):
    """
 >>>  Add up two integer numbers.
      This function simply wraps the ``+`` operator.

 >>>  Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

 >>>  Returns
    -------
        The sum of ``num1`` and ``num2``.

 >>>  Examples
    --------
    >>> add(3, 7)
    10
    >>> add(27, -24)
    3
    """
    return num1 + num2

c = add(7,3)
print(c)
d = add(10,7)
print(d)