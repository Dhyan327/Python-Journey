# In this part I will learn about "Getters and  Setters"

""" Getters in Python are methods that are used to access the values of an object's properties.
    They are used to return the value of a specific property, and are typically defined using the @property decorator. """

""" It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
    For that we need setter method which can be added by decorating method with @property_name.setter  """

class Myclass:
    def __init__(self, val):
        self.value = val

    def show(self):
        print(f"value is {self.value}")

    @property
    def ten_value(self):
        return f"Ten time of {self.value} is {10 * self.value}"
    
    @ten_value.setter
    def ten_value(self,new_value):          # Setter method 
        self.value = new_value/10

a = Myclass(3)
print(a.value)
a.show()
print(a.ten_value)      
print()

# Now, if we want to set the value of "ten_value" the we cannot change it as follow :- "a.ten_value = 50" . To do that we have to use setter method.
""" It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
    For that we need setter method which can be added by decorating method with @property_name.setter"""

a.ten_value = 70
a.show()
print(a.ten_value)

# Conclusion :~~>
""" In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden.
    This can be useful for encapsulation and data validation."""