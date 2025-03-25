# In this part I will learn about "Static Methods" in Python

""" Static methods in Python are methods that belong to a class rather than an instance of the class.
    They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self).
    They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.
"""
class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num += n
    
    @staticmethod
    def add(a,b):
        return a+b
    
obj = Math(7)
print(obj.num)
obj.addtonum(3)
print(obj.num)

print(obj.add(3,4))
print(Math.add(7,3))       # Here, instead of using object name "obj" we can also write the class name "Math"