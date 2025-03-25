# In this part I will learn about "List Method"

# 1st Method :--> [Append Method]
l = [1,2,3,4,5,6]
print(l)
l.append(7)         # This method will add the item at the end of the existing list.
print(l)            # Note : The Append Method can take exactly one argument

print("\n")

# 2nd Method :--> [sort Method]
a = [7,27,3,73,37,54,33]
print(a)
a.sort()                  # This method sorts the list in ascending order. Now, The original list is updated
print(a)
a.sort(reverse = True)    # If we want to print the list in descending order then We must have to give reverse=True as a parameter in the sort method.
print(a)                  # Note: Do not mistake the reverse parameter with the reverse method.

colors = ["voilet", "orange", "blue", "green"]  
colors.sort()                   # In Ascending order
print(colors)       
colors.sort(reverse=True)       # In Descending order 
print(colors)

print("\n")

# 3rd Method :--> [Reverse Method]
x = [1,2,3,4,5,6,7,8,9,10]
print(x)
x.reverse()             # The Reverse Method will reverse the order of the list
print(x)

print("\n")

# 4th Method :--> [Index Method]
colors = ["voilet", "orange", "blue", "green"]
print(colors)  
print("The index number of 'green' is :",colors.index("green"))         # The index method will return the index of the first occurrence of the list item.

print("\n")

# 5th Method :--> [Count Method]
num = [1,2,3,3,4,5,6,7,7,7,8,9]
print(num)
print("The count of '7' in the list is :",num.count(7))

print("\n")

# 6th Method :--> [Copy Method]
b = [0,2,3,4,5,6] 
print(b)            
d = b.copy()        # This method will Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
d[0] = 1
print(d)

colours = ["voilet", "green", "indigo", "blue"]
print(colours)
newlist = colours.copy()
newlist[0] = "Red"
newlist[2] = "Orange"
print(newlist)

print("\n")

# 7th Method :--> [Insert Method]
a = [7,27,3,73,37,54,33]
print(a)
a.insert(3, 77)         # This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
print(a)

print("\n")

# 8th Method :--> [Extend Method]
f = [1,2,3,4,5,6,7,8,9,10]
print(f)
g = [10,9,8,7,6,5,4,3,2,1]
print(g)
f.extend(g)            # This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list
print(f)                 

print("\n")

# There is an another alternative of Extend Function i.e. concatenating the lists
i = [1,2,3,4,5,6,7,8,9,10]
x = [10,9,8,7,6,5,4,3,2,1]
h = i + x
print(h)

rc = ["voilet", "indigo", "blue", "green"]
cd = ["yellow", "orange", "red"]
print(rc + cd)