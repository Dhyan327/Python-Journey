# In this part I will learn about "F-String"
'''It is a new string formatting mechanism introduced by the PEP 498.
 It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal).
 The primary focus of this mechanism is to make the interpolation easier.'''

# First, The String Formatting was done in python using the format method.
# Example :-->
letter = "Hey, My name is {} and I am from {}"
name = "Dhyan"
country = "India"

print(letter.format(name, country))
letter = "Hey, My name is {1} and I am from {0}"
print(letter.format(country, name))

# F-Stings In Python :-->
'''When we prefix the string with the letter 'f', the string becomes the f-string itself.
 The f-string can be formatted in much same as the str.format() method.
 The f-string offers a convenient way to embed Python expression inside string literals for formatting.'''

# Example :-->
print(f"Hey, My name is {name} and I am from {country}")
print(f"Hey, My name is {{name}} and I am from {{country}}")      # If we want to display as it is in the string then we have to add another curly brackets as shown
print("\n")

# Example Given in Tutorial :-->
txt = "For only {price:.2f} dollars!"         # Here, 2f means to round up to two decimal places 
print(txt.format(price = 49.999))             # So, here the price will become 50 dollars 
# If we want to run the following code in F-String then :-->
p = 49.999
print(f"For only {p:.2f} dollars!")

print("\n")

# Example Given in Tutorial :-->
# 1st Example :-
val = 'Geeks'  
print(f"{val} for {val} is a portal for {val}.")  
# In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

name = 'Dhyan'        
age = 16              
print(f"Hello, My name is {name} and I'm {age} years old.")

print("\n")

# 2nd Example :-
print(f"{2 * 50}")
print(type(f"{2 * 50}"))