# In this part I will learn about "Joining Sets"
'''Sets in python more or less works in the same way as sets in mathematics.
 We can perform operations like union and intersection on the sets just like in mathematics.'''

'''# 1st operation :~~> [Union and Update]'''
# The union() and update() methods prints all items that are present in the two sets
# Example :-->
s1 = {1,2,5,6,7}
s2 = {3,4,6,7}
print(s1.union(s2))     # The union() method returns a new set
print(s1)               # Here, after the implementation of union method the "s1" set will remain same only.
s1.update(s2)           # whereas update() method adds item into the existing set from another set.
print(s1)               # But, after the implementation of update method "s1" will be changed

# Example given in Tutorial :-->
cities = {"Tokyo", "Paris", "Sydney", "Mumbai"}
cities2 = {"Tokyo", "London", "Mosco", "Paris"}
cities3 = cities.union(cities2)
print(cities3)
cities.update(cities2)
print(cities)

print("\n")

'''2nd operation :~~> [Intersection and Intersection_update]'''
# The intersection() and intersection_update() methods prints only items that are common to both the sets. 
# Example :-->
s1 = {1,2,3,5,7}
s2 = {3,4,6,7}
print(s1.intersection(s2))          # The intersection() method returns a new set
print(s1)                           # Here, after the implementation of intersection method the "s1" set will remain same only.
s1.intersection_update(s2)          # whereas intersection_update() method updates into the existing set from another set.
print(s1)                           # But, after the implementation of intersection_update method "s1" will be changed

# Example given in Tutorial :-->
cities = {"Tokyo", "Paris", "Sydney", "Mumbai"}
cities2 = {"Tokyo", "London", "Mosco", "Paris"}
cities3 = cities.intersection(cities2)
print(cities3)
cities.intersection_update(cities2)
print(cities)

print("\n")

'''3rd operation :~~> [Symmetric_Difference and Symmetric_Difference_update]'''
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets
# Example :-->
s1 = {1,2,5,6,7}
s2 = {3,4,6,7}
print(s1.symmetric_difference(s2))      # The symmetric_difference() method returns a new set 
print(s1)                               # Here, after the implementation of symmetric_difference method the "s1" set will remain same only.
s1.symmetric_difference_update(s2)      # whereas symmetric_difference_update() method updates into the existing set from another set.
print(s1)                               # But, after the implementation of symmetric_difference_update method "s1" will be changed  

# Example given in Tutorial :-->
cities = {"Tokyo", "Paris", "Sydney", "Mumbai"}
cities2 = {"Tokyo", "London", "Mosco", "Paris"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
cities.symmetric_difference_update(cities2)
print(cities)

print("\n")

'''4th operation :~~>  [Differnce and Difference_update]'''
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets
# Example :-->
s1 = {1,2,5,6,7}
s2 = {3,4,6,7}
print(s1.difference(s2))        # The difference() method returns a new set
print(s1)                       # Here, after the implementation of difference method the "s1" set will remain same only.
s1.difference_update(s2)        # whereas difference_update() method updates into the existing set from another set.
print(s1)                       # But, after the implementation of difference_update method "s1" will be changed

# Example given in Tutorial :-->
cities = {"Tokyo", "Paris", "Sydney", "Mumbai"}
cities2 = {"Tokyo", "London", "Mosco", "Paris"}
cities3 = cities.difference(cities2)
print(cities3)
cities.difference_update(cities2)
print(cities)