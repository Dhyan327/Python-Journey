# In this part I will learn about "Enumerate Function"

"""The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string),
   and get the index and value of each element in the sequence at the same time."""

# Examples :~~.
marks = [3,27,10,7,30,17]

# Traditional method :-->
index = 0
for i in marks:
    print(i)
    if index == 3:
        print("Congrats!!!")
    index += 1
print("")

# Enumerate method :-->
for index,i in enumerate(marks):
    print(i)
    if index == 3:
        print("Congrats!!!")
print("")

# Example [given in Tutorial] :~~>
fruits = ['apple', 'banana', 'mango']       
for v in enumerate(fruits):                 
    print(v)                                
print("")

"""The Enumerate function returns a tuple containing the index and value of each element in the sequence.
   You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.
"""

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
print("")


"""Changing the Start Index :~~>"""
# By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function.

for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")
print("")

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits,start=1):
    print(f"{index}: {fruit}")
print("")

# Examples with Tuple and String :~~>

tup = ('red', 'green', 'blue')
for index, color in enumerate(tup):
    print(f"{index} : {color}")
print("")

string = 'Dhyan'
for index, c in enumerate(string,start=1):
    print(f"{index} = {c}")