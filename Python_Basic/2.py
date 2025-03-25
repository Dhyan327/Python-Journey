# In this Part I will learn about Datatypes  

a = 3               # This Datatype is called "integer" type
a1 = 7.3            # This Datatype is called "float" type
a2 = complex(7, 3)  # This Datatype is called "complex" type
b = True            # This Datatype is called "boolean" type
c = "Dhyan"         # This Datatype is called "string" type
d = None            # This Datatype is called "None" type

list  = [8, 7.3, [-8, 7], ["Apple", "Samsung"] ]    # This Datatype is called list type
print(list)

tuple = (8, 7.7, [-8, 7], ["Lion","Tiger"] )        # This Datatype is called tuple type 
print(tuple)

dict = {"Name": "Dhyan", "Age":16, "Canvote":True}  # This Datatype is called dictionary type
print(dict)
print("\n")

# We can find the type of the variable by using type() function as shown :-->
print("The type of a is ", type(a))
print("The type of a1 is ", type(a1))
print("The type of a2 is ", type(a2))
print("\n")
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of d is ", type(d))
print("\n")
print("The type of list is", type(list))
print("The type of list is", type(tuple))
print("The type of list is", type(dict))