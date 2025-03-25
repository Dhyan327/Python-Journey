# In this part I will learn about "Accessing list item/element" and "Range of list"
# We can access list item by using its index with the square bracket syntax[] 
''' There are "Two" types of Accessing list item i.e.
1 :~~> Positive Indexing 
2 :~~> Negative Indexing '''

colors = ["Red", "Green", "Blue", "Orange", "White"]
#          [0]     [1]     [2]      [3]      [4]      ~~>    "Positive Index Number"
#          [-5]    [-4]    [-3]     [-2]     [-1]      ~~>   "Negative Index Number"

# Example given in Tutorial :--> [Positive Indexing]
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[4])

print("\n")

# Example :--> [Negative Indexing]
''' Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. 
The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.'''
# We have to first convert Negative index into Positive index by understanding the given syntax i.e. print(variable_name[len(variable_name)-index given]) 
print(colors[-1])      # Here, the interpreter will understand it like print(colors[len(colors)-1]) and will print "White" 
print(colors[-2])      # Here, the interpreter will understand it like print(colors[len(colors)-2]) and will print "Orange"
print(colors[-3])      # Here, the interpreter will understand it like print(colors[len(colors)-3]) and will print "Blue"
print(colors[-4])      # Here, the interpreter will understand it like print(colors[len(colors)-4]) and will print "Green"
print(colors[-5])      # Here, the interpreter will understand it like print(colors[len(colors)-5]) and will print "Red"

print("\n")

# Range of strings :~~>
# We can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip the iteration in between the range then :-
'''Syntax=
listname = (start | end | jump_index)'''
# Here, we have to provide the index of the element from where we want to start and the index of the element till which we want to print the value
'''Note :~~>
1 :--> Jump index is optional
2 :--> The element of the end index number will not be included'''

Marks = [3, 5, 7, 7.3, 5.7, 2.7, 9, 5.1, 7.2, 3.7]
print(Marks)           # If we want to print the whole list we can do this two methods
print(Marks[:])        # When no index is provided, the interpreter prints all the values till the ends
print(Marks[2:])       # This will start printing from the second index number of the string
# Example of pulsing Negative Index
print(Marks[-7:-1])    # The interpreter will understand the command as follow :- print(Marks[len(Marks)-5:len(Marks)-1]) i.e. print(marks[2:6]) 
# Example with Jump Index
print(Marks[::2])      # Here we have not provided start and end index which means all the values will be print. But as we have provided a jump index of '2' only alternate values will be printed
print(Marks[1::3])