# In this part I will learn about "Sets in Python" and "Accessing set items"
'''
~~> Sets are unordered collection of data items. 
~~> They store multiple items in a single variable. 
~~> Set items are separated by commas and enclosed within curly brackets {}. 
~~> Sets are unchangeable, meaning you cannot change items of the set once created. 
~~> Sets do not contain duplicate items.'''

s = {2,3,7,3}
print(s)

info = {"Dhyan", 27, True, 7.3, 27}
print(info)     # Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set
i ={}               # This is a wrong way to make an Empty set 
print(type(i))      # By doing this the Type will be "Dictionary" because the syntax of Dictionary is same as Set

# For making "Empty Set" :-  [Example]
Dhyan = set()
print(type(Dhyan))

print("\n")

# Accessing set items :~~>
# You can access items of set using a for loop.
 
# Example :-->
for i in info:
    print(i)
# Note :- Here, The order of the item will be occured in random order 