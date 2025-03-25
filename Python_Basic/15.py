# In this part I will learn about "For loop" statement 
# Sometimes the programmer needs to execute a group of statement a certain number of times. This can be done using loops.
# Loops are classified into following types :- For loop, While loop and Do- while loop 

# Examples of "For Loop" in string Datatype
name = "Dhyani"
for a in name:
    print(a, end="___\n")
    if (a == "n"):
        print("This is something special")
print("\n")

# Example of "For Loop" in list Datatype
colors = ["Red", "Green", "Blue", "Orange"]     
for x in colors:
    print(x)
    for i in x:     # In list we can also iterate the string. Eg- Here, "Red" is a string in list "Colors". So, we can also iterate "Red" as R,e,d.    
        print(i)