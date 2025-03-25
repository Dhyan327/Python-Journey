# In this part I will learn about "Tuple" datatype of python and "Tuple Indexing" and "Range of Index"
'''
~~> Tuples are ordered collection of data items.
~~> They store multiple items in a single variable.
~~> Tuple items are separated by commas and enclosed within round brackets ().
~~> Tuples are unchangeable meaning we can not alter them after creation.'''        # Tuples are immutable i.e they cannot be changed
v = (7)                # If we write only one element in the tuple then the interpreter will understand the variable as integer. So, it will return the value as integer 
print(type(v), v)      # so, if we only write one item in the tuple then we must have to write comma after such as v = (7,) then only it will return the value as tuple

tup = (1,2,3,27,273,37,"Green",True)
print(type(tup), tup)
# tup[0] = 0           # If we run this command then it will return error because tuple cannot be changed 

# Tuple Indexing :~~>
# Example :-->
print(tup[0])
print(tup[-6])         # Negative Indexing 
print(tup[3])          # Positive Indexing    

# We can check if a given item is present in the tuple. This is done using the "in" keyword.
# Example :-->
if 273 in tup:
    print("Yes, 273 is present in this tuple")

# Example given in Tutorial :-->
country = ("Spain", "Italy", "India", "England", "Germany")
if "India" in country:
    print("India is present.")
else:
    print("India is absent.")

print("\n")

# Range of Index :~~.
# You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.
'''Syntax=
listname = (start | end | jump_index)'''        # Note :--> jump Index is optional
tup2 = tup[2:6]
print(tup2)

# Example given in Tutorial :-->
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])            # Note: The element of the end index provided will not be included 
print(animals[-7:-2])             
print(animals[::2])    # Here, we have not provided start and end index, that means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.
print(animals[-8:-1:2])
print(animals[1:8:3])         # Here, jump index is 3. Hence it prints every 3rd element within given index.