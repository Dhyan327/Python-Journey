# In this part I will learn about "List  Comprehension"
# List Comprehension are used for creating new list from other iterables like list, tuples, dictionaries, sets and even in array and strings

''' Syntax :~~>
List = [Expression(item) for item in iterable if condition]'''
# Expression :-  It is the item which is being iterated
# Iterable :- It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition :- Condition checks if the item should be added to the new list or not.

# Example :-->
lst = [i for i in range(7)]
print(lst)
lst = [i*i for i in range(7)]
print(lst)
lst = [i*i for i in range(7) if i%2==0]
print(lst)

print("\n")

# Example given in Tutorial :-->

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]   # This example will accept the item with the smaller letter "0" in the new list 
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names1 = ["Dhyan", "Om", "Purva", "Het", "Krunal"]        # This example will accept the item which have more than four letters 
namesWith_4 = [i for i in names1 if (len(i) > 4)]
print(namesWith_4)