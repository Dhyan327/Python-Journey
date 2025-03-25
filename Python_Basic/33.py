# In this part I will learn about "Recursion in Python"
# Recursion is the process of defining something in terms of itself.

# Python Recursive Function :-->
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

''' Factorial :->   [Just for explanation]'''
#  factorial(7) = 7*6*5*4*3*2*1
#  factorial(6) = 6*5*4*3*2*1
#  factorial(3) = 3*2*1
#  factorial(1) = 1
#  factorial(0) = 1   

# Now, from the above example we ca say that :- factorial(n) = n * factorial(n-1)

# Example given in Tutorial :-->
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print("The factorial of 0 is :",factorial(0))
print("The factorial of 3 is :",factorial(3))
print("The factorial of 7 is :",factorial(7))

print("\n")

# Just for explanation that how the above function works :->
# EG: print(factorial(5))
# factorial(n) = n * factorial(n-1)
''' 
1st Step:- 5 * factorial(4)
2st Step:- 5 * 4 * factorial(3)
3st Step:- 5 * 4 * 3 * factorial(2)
4st Step:- 5 * 4 * 3 * 2 * factorial(1)
5st Step:- 5 * 4 * 3 * 2 * 1    
''' 

# Quick Quiz: Write a program to print the Fibonacci sequence
'''Fibonacci sequence :-> [Just for explanation]'''
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)

# Now, from the above example we ca say that :-  f(n) = f(n-1) + f(n-2)
def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return f(n-1) + f(n-2)
    
print("The Fibonacci Sequence of 0 is :",f(0))
print("The Fibonacci Sequence of 3 is :",f(3))
print("The Fibonacci Sequence of 7 is :",f(7))