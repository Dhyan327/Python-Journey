# In this part I will learn about "Operator Overloading" in Python

""" Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. 
    This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, 
    just as you would for built-in data types like int, float, and str. Operator overloading allows you to create more readable and intuitive code. """

# How to overload an operator in Python?
""" You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). 
    Here are some of the most commonly overloaded operators and their corresponding special methods:  """
"""
+ : __add__         - : __sub__
* : __mul__         / : __truediv__
< : __lt__          > : __gt__
== : __eq__ """
# Note :~~> It's important to note that operator overloading is not limited to the built-in operators, you can overload any user-defined operator as well.

# Example :~~>
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, x):
        # return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"      # Here, if we do like this then the resultant vector will be a string, but we want the resultant vector as a vector 
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
v1 = Vector(1,2,3)
print(v1)
v2 = Vector(3,5,7)
print(v2)

print(v1+v2)
print(type(v1+v2))
print()

# Example :~~>
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(round(real,2), round(imag,2))

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

print(c1)
print(c2)

print(c1 + c2)          # Adding two complex numbers / Output: 3 + 7i
print(c1 - c2)          # Subtracting two complex numbers / Output: 1 + -1i
print(c1 * c2)          # Subtracting two complex numbers / Output: -10 + 11i 
print(c1 / c2)          # Dividing two complex numbers / Output: 0.82 + -0.29

# Conclusion :~~>
""" Operator overloading is a powerful feature in Python that allows you to create more readable and intuitive code. 
    By redefining the behavior of mathematical and comparison operators for custom data types, you can write code that is both concise and expressive. 
    However, it's important to use operator overloading wisely, as overloading the wrong operator or using it inappropriately can lead to confusing or unexpected behavior.
"""