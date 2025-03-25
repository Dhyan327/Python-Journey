# In this part I will learn about "Set Methods"
# There are several in-built methods used for the manipulation of set.They are explained below :-

# 1st Method :- [Isdisjoint Method]
# The isdisjoint() method checks if items of given set are present in another set.
cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities2 = {"Tokyo", "Sydney", "Mosco", "Paris"}
print(cities.isdisjoint(cities2))       # This method returns False if items are present, else it returns True.

# 2nd Method :- [Issuperset Method]
# The issuperset() method checks if all the items of a particular set are present in the original set. 
cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities2 = {"Tokyo", "Sydney", "Mosco", "Paris"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Mumbai", "Paris"}      # It returns True if all the items are present, else it returns False.
print(cities.issuperset(cities3))

# 3rd Method :- [Issubset Method] 
# The issubset() method checks if all the items of the original set are present in the particular set
cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities3 = {"Tokyo", "Mumbai", "Paris"}      
print(cities3.issubset(cities))

print("\n")

# 4th Method :- [Add Method]
# If you want to add a single item to the set use the add() method.
cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities.add("Los Vegas")     # Note :- "Add" Method can take only one argument
print(cities)

# 5th Method :- [Update Method]
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities2 = {"Tokyo", "Sydney", "Mosco", "Paris"}
cities.update(cities2)
print(cities)

print("\n")

# 6th Method :- [Remove/Discard Method]
# We can use remove() and discard() methods to remove items form list.
# The main difference between remove and discard is that, if we try to remove an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities.discard("Tokyo")
print(cities)                        # Note :- Both Remove and Discard Method can remave only one argument 

cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities.remove("Paris")
print(cities)              

cities = {"Tokyo", "Paris", "London", "Mumbai"}
# cities.remove("Mosco")            # Here, it will give keyword error as output
cities.discard("Mosco")             # Here, it will not raise error as output  
print(cities)  

print("\n")

# 7th Method :- [Pop Method]
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered.
# However, you can access the popped item if you assign the pop() method to a variable.
cities = {"Tokyo", "Paris", "London", "Mumbai"}
print(cities)
item = cities.pop()
print(cities,item)

# 8th Method :- [Del Method]
# This method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Paris", "London", "Mumbai"}
del cities              
# print(cities)         # Here, we will get an error because our entire set has been deleted and there is no variable called cities which contains a set.

# 9th Method :- [Clear Method]
# This method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Paris", "London", "Mumbai"}
cities.clear()
print(cities)

# 10th Method :- [Check if item exists]
# You can also check if an item exists in the set or not.
info = {"Dhyan", 27, True, 7.3, 27}
if "Dhyan" in info:
    print("Dhyan is present")
else:
    print("Dhyan is Absent")