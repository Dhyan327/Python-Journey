# In this learn about "Dictionaries in Python" and "Dictionaries items"
'''
~~> Dictionaries are ordered collection of data items.
~~> They store multiple items in a single variable.
~~>  Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.'''

# Example :-->
dic = {
    3 : "Dhyan",
    7 : "Dhoni",
    18: "Virat"
}
print(dic)
print(dic[3], dic[18])
print("\n")

# Making Empty Dictionary :~~>
d = {}
print(d)
print(type(d))
print("\n")

# Accessing Dictionary items :~~>

info = {'name':'Dhyan', 'age':17, 'eligible':True}
print(info) 
print("\n")

'''# I. Accessing single values :-->'''
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
# Difference :- 
print(info['name'])
# print(info['name2'])        # Here, it will give error becouse 'name2' is not defined in variable 
print(info.get('name2'))      # Wherein, here it will give 'none' as an output 
print(info.get('age'))
print(info.get('eligible')) 
print("\n")

'''II. Accessing keys :-->'''
# We can print all the keys in the dictionary using keys() method.
print(info.keys())

'''III. Accessing multiple values :-->''' 
# We can print all the values in the dictionary using values() method.
print(info.values())
print("\n")

# We can also print the values similarly by the following method 
for key in info.keys():
    print(f' The value corresponding to the key "{key}" is : {info[key]}')
print("\n")

'''IV. Accessing key-value pairs :-->'''
# We can print all the key-value pairs in the dictionary using items() method.
print(info.items())
print("\n")

# We can also print the key-value pairs similarly by the following method 
for key,value in info.items():
    print(f" The value corresponding to the key \"{key}\" is : {value}")