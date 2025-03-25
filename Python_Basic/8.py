# In this part I will learn about string methods and operation

a = "Dhyan"       # String are immutable i.e. they cannot be changed
print(len(a))
print(a.lower())  # This function i.e. upper and lower functions will not change the string value but will operate on the string and make a new string 
print(a.upper())

print("\n")

b = "Dhyani!!!"
print(b.rstrip("!"))    # The rstripe function will not remove the leading trailing character i.e. if b = "!!Dhyani!!" then it will display the result as "!!Dhyani"
print(b.replace("Dhyani", "Dhyan"))         # The replace function will replace the value given in the string with the another value

print("\n")

c = "~~~Dhyan~~~ `````` ~~~Dhyan~~~"
print(c.split(" "))         # The split function will change the string into list
print(type(c.split(" ")))   # If we print the type of this variable then it will return as a list 
print(c.count("Dhyan"))     # The count function will tell the number of time the given value has occured within the given string 

print("\n")

d = "Welcome to the python!"
print(d.endswith("!"))  # The endswith function checks if the string ends with a given value. If "Yes" then it will return "True", else return "False" 
print(d.endswith("to", 5, 10))  # We can also check for a value in-between the string by providing start and end index position
print(d.startswith("Welcome"))  # The startswith function checks if the string strats with a given value. If "Yes" then it will return "True", else return "False" 

print("\n")

print(d.find("python"))     # The find function searches for the first occurence of the given value and returns the index where it is present 
print(d.find("Dhyan"))      # If the given value is absent from the string then it returns "-1" as output
print(d.index("python"))    # The index function is same as find but in find function if the value is absent from the string then it returns "-1" as output but
# print(d.index("Dhyan"))   # In index function if the given value is absent from the string then it throws an error 