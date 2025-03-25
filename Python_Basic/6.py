# In this part I will learn about "Accessing characters of string and Looping through the string"

# This is an example for Accessing characters of strings 
name = "Dhyan"
print(name)
print("\n")
print(name[0])           # This will display "D"
print(name[1])           # This will display "h"
print(name[2])           # This will display "y"
print(name[3])           # This will display "a"
print(name[4])           # This will display "n"
print("")

# This is an example for Looping through the Single-line strings  
for i in name:
    print(i)

# This is an example for Looping through the Multi-line strings  
a = """ 
    Hi Dhyan,
    How are you?
    """
print(a) 
for character in a:
    print(character, end=" ")