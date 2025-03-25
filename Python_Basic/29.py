# In this part I will learn about "Operation on Tuple" and "Tuple Method"
# Manipulating Tuples :~~>
''''Tuples are immutable, hence if you want to add, remove or change tuple items, 
then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.'''

# Example given in Tutorial :-->
countries = ("Australia", "France", "England", "Germany", "India")
temp = list(countries)
temp.append("Russia")       # ading item 
temp.pop(3)                 # removeing item
temp[2] = "Israel"          # changing item
countries = tuple(temp)
print(countries)            # Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

# However, we can directly concatenate two tuples without converting them to list.
countries1 = ("china", "America", "Bhutan", "SriLanka")
countries2 = ("India", "Israel", "Russia")
i = countries1 + countries2
print(i)

print("\n")

# Tuple Method :~~>
# As tuple is immutable type of collection of elements it have limited built in methods

# 1st Method:--> [Count Method]
tuple1 = (1,2,3,4,3,5,6,7,8,7,9,7)
res = tuple1.count(7)                   # The count() method of Tuple returns the number of times the given element appears in the tuple
print('Count of 7 in Tuple1 is  :', res)

# 2nd Method :--> [Index Method]
''' Syntax :->'''               # Note: This method raises a ValueError if the element is not found in the tuple.
# Tuple.index(element, start, end)
tuple2 = (1,2,3,4,3,5,6,7,8,7,9,7)
res1 = tuple2.index(7)          # The Index() method returns the first occurrence of the given element from the tuple.
print('First occurrence of 7 is :', res1)

tup1 = [0,1,2,3,2,3,1,3,2,3]
a = tup1.index(3,4,7)
print("First Occurence of 3 between 4th index to 7th index is :",a)