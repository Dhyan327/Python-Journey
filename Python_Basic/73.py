# In this part I will learn about "Walrus Operator"

""" The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. 
    This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation. """
# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

# Examples :~~>

happy = False
print(happy)
print(happy := True)
print()

# Example with While loop :~~>

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())
print()

# The following is a Traditional way of the above example :-
"""
while True:
   food = input("What food do you like?: ")
   if food == "quit":
       break
   foods.append(food) """

food = list()
while (f := input("What food do you like? : ")) != "quit":
    food.append(f)
print()

# Example with If statement :~~>

names = ["Harsh","Nilabh","Abhishek","Jainil","Dhyan","Krunal","Om"]
if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")

# Conclusion :~~>
""" In conclusion, the Walrus Operator is a useful tool for Python developers to have in their toolkit. 
    It can help streamline code and reduce duplication, but it should be used with care to ensure code readability and maintainability.
    It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused. """