# In this part I will learn about the difference between "is" keyword and "==" operator.

# In Python, is and == are both comparison operators that can be used to check if two values are equal.
# However, there are some important differences between the two that you should be aware of.

# The "is" operator compares the identity of two objects, while the "==" operator compares the values of the objects.
# This means that "is" will only return True if the objects being compared are the exact same object in memory, while "==" will return True if the objects have the same value.

"""
~~> One important thing to note is that, in Python, strings, tuples and integers are immutable, which means that once they are created, their value cannot be changed.
    This means that, for strings, integers and tuple, "is" and "==" will always return the same result.
~~> For mutable objects such as lists and dictionaries, "is" and "==" can behave differently"""

# Examples :~~>

a = 3
b = "3"
print(a is b)   # False
print(a == b)   # False
print()

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)   # False
print(x == y)   # True
print()

m = "Dhyan"
n = "Dhyan"
print(m is n)   # True
print(m == n)   # True
print()

i = 7
j = 7
print(i is j)   # True
print(i == j)   # True
print()

c = (1, 2, 3)
d = (1, 2, 3)
print(c is d)   # True
print(c == d)   # True
print()

g = None
k = None
print(g is k)       # True
print(g == k)       # True

print(g is None)    # True
print(g == None)    # True
print()

# In conclusion :~~>
"""The "is" keyword is used to check the exact location of the object in the memory while the "==" operator is used to compare the value of the object.
 In general, you should use "==" when you want to compare the values of two objects, and use "is" when you want to check if two objects are the same object in memory."""