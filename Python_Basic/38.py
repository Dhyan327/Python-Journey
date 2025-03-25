# In this part I will learn about "Dictionary Methods"
# Dictionary uses several built-in methods for manipulation.They are listed below

ep1 = {3:77, 7:73, 10:89, 17:89}
ep2 = {27:43, 30:90}
print(ep1)
print(ep2)
info = {'name':'Dhyan', 'age':16, 'eligible':True}
print(info)
print("\n")

# 1st Method :--> [Update Method]
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
ep1 = {3:77, 7:10, 10:89, 17:89}
ep2 = {27:43, 30:90, 3:27, 7:10}
ep1.update(ep2)     # Here, the value of key "3" is changed to "27" from "77"
print(ep1)

info = {'name':'Dhyan', 'age':16, 'eligible':True}
info.update({'age':17})
info.update({'DOB':2007})
print(info)
print("\n")

# 2nd Method :--> [Clear Method]
# The clear() method removes all the items from the list.
ep1 = {3:77, 7:73, 10:89, 17:89}
ep1.clear()
print(ep1)

info = {'name':'Dhyan', 'age':16, 'eligible':True}
info.clear()
print(info)
print("\n")

# 3rd Method :--> [Pop Method]
# The pop() method removes the key-value pair whose key is passed as a parameter.
ep1 = {3:77, 7:73, 10:89, 17:89}
ep1.pop(10)
print(ep1)

info = {'name':'Dhyan', 'age':16, 'eligible':True}
info.pop('age')
print(info)
print("\n")

# 4th Method :--> [Popitem Method]
# The popitem() method removes the last key-value pair from the dictionary.
ep1 = {3:77, 7:73, 10:89, 17:89}
ep1.popitem()
print(ep1)

info = {'name':'Dhyan', 'age':16, 'eligible':True}
info.popitem()
print(info)
print("\n")

# 5th Method :--> [Del Method]
# we can also use the del keyword to remove a dictionary item.
ep1 = {3:77, 7:73, 10:89, 17:89}
del ep1[10]
print(ep1)

info = {'name':'Dhyan', 'age':16, 'eligible':True}
del info['age']
print(info)
del info        # If key is not provided, then the del keyword will delete the dictionary entirely.
# print(info)   # Here, we will get an error because our entire dictionary has been deleted and there is no variable called "info" which contains a Dictionary