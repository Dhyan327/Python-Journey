# In this part I will learn about "Decorators in Python"

# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. 
# They are a way to extend the functionality of a function or method without modifying its source code.

# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.

""" A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function (which is taken as an argument). 
    The new function is often referred to as a "decorated" function. """

# The basic syntax for using a decorator is the following :
"""
@decorator_function
def my_function():
    pass
"""

# The "@decorator_function" notation is just a shorthand for the following code :
"""
def my_function():
    pass
decorator_function(my_function) ()
"""

# Example :~~>

def greet(fx):
    def mfx(*args,**kwargs):
        print("Hello, you are welcome from Dhyan")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def myfunc():
    print("How are you?")

myfunc()            # This both method is same!!
# greet(myfunc)()       # But if we do like this then be sure that "@greet" statement before th "myfunc()" function should be removed otherwise it decorate it twisly!
print()

def add(a,b):
    print(f"The sum of {a} and {b} id {a+b}")
greet(add)(7,3)


# Conclusion :~~>
""" In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code.
    They are used for a variety of purposes, such as logging, memoization, access control, and more.
    They are a powerful tool that can be used to make your code more readable, maintainable, and extendable."""