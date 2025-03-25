# In this part I will learn about "string slicing"

# These are the examples for finding length of an string
names = "Dhyan,Om,Krunal"
print(len(names))       # By len() function we can find the length of the string 
print(names[0:5])       # This will include [0] but not [5]
print("\n")

fruit = "orange"
a = len(fruit)
print("Orange is an", a,"letter word")
print("\n")

print(fruit[:5])    # If we do not write 0 then the python interpreter will automatically add 0
print(fruit[1:5])   # This will include [1] but will not include [4]
print(fruit[:])     # If we dont write any number then it will display the whole string  
print(fruit[0:-3])  # if we do negative slicing then the python interpreter will understand like this --> print(fruit[0:len(fruit)-3]) i.e. like print(fruit[0:3])
print(fruit[-5:-2]) # if we do negative slicing like this then the python interpreter will understand like this --> print(fruit[len(fruit)-5:len(fruit)-2]) i.e. like print(fruit[1:4])
print(fruit[-1:-3]) # This will print nothing as there is no sense in doing negative slicing