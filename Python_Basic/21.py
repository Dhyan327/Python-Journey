# In this part I will learn about "Python Function"
# A function is a block of code that performs a specific task whenever it is called.
# In bigger program when we have large amount of code, it is advisable to create or use existing function that make the program flow organised and neat.
"""
There are two types of function :
1 :--> Build- in function
2 :--> User- Defined function
""" 
# The function which are defined and pre-coded in python are called "Build-in Function " 
# Example :--> min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc.
# The functions which are created by the programmer to perform specific task as per need, such function are called "User- Defined Function"

# Examples :-->[User Define function]
# The function for finding "Geometric Mean"
def calculategmean(a,b):
    mean =  (a*b)/(a+b)
    print(mean)
# The function for finding "The Greater Number"
def isgreater(a,b):
    if(a>b):
        print("First Number is Greater")
    elif(a==b):
        print("Both Number are Equal")
    else:
        print("Second Number is Greater")
""" 
If sometimes the programmer writing a big program wants to define the function,but wanted to write the body of the function afterwards,
then instead of writing body of the function he has to write pass function like below,   
"""
# The function with pass function
def islesser(a,b):
    pass                # If we will not write pass then it will give error as output

# 1st Example with Traditional Method 
a = int(input("Enter the First Number :"))
b = int(input("Enter the Second Number :"))
# Finding which number is Greater with Traditional Method
if(a>b):
    print("First Number is Greater")
elif(a==b):
    print("Both Number are Equal")
else:
    print("Second Number is Greater")
# Finding the mean of the two number with Traditional Methof    
gmean = (a*b)/(a+b)
print("The Geometric mean of the two number is :",gmean)      

print("\n")

# 2nd Example with Function Method 
c = int(input("Enter the First Number :"))
d = int(input("Enter the Second Number :"))           
calculategmean(c,d)         # Now, To find the Geometric Mean we do not have to do the method used in the First Example,  
isgreater(c, d)             # Now, To find the Greater Number we do not have to do if-else statement as used in the First Example, but have to use the function 