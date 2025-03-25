# In this part I will learn about "List" Datatype of python and "List index"
'''
~~> List are ordered collection of data items
~~> They store multiple items in a single variable
~~> List items are prepared by commas and enclosed within square brackets i.e.--> []
~~> List are "changeable" meaning we can alter them after creation'''
# Examples :-->
marks = [3,5,7]       # This are the "Marks" of the students
print(marks)
print("The marks of student 'A' is :",marks[0])
print("The marks of student 'B' is :",marks[1])
print("The marks of student 'C' is :",marks[2])
# print("The marks of student 'C' is :",marks[3])       # If the value is out of the range then the interpreter will give an error as output 
print("\n")
a = [8, 7.3, [-8, 7], ["Apple", "Samsung"], True ]     # In the list we can add all types of 'Datatypes' i.e. "integer, float, complex, string, boolean, none" etc.
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print("\n")

# We can check if a given item is present in the list. This is done using the "in" keyword as shown below
if 7.3 in a:
    print("Yes, 7.3 is present in 'a'")
else:                                       # Here, 7.3 is present in variable "a", so it will return "Yes"
    print("No, 7.3 is not present in 'a'")

if ["Apple", "Samsung"] in a:
    print("Yes, Apple and Samsung is present in 'a'")
else:                                                       # Here, the string ["Apple", "Samsung"] are present in variable "a", so it will return "Yes"
    print("No, Apple and Samsung is not present in 'a'")

if 3 in a:
    print("Yes, 3 is present in 'a'")
else:                                       # Here, 3 is present in variable "a", so it will return "Yes"
    print("No, 3 is not present in 'a'")

if "Apple" in ["Apple", "Samsung"]:
    print("Yes")
else:                       # Same things applies for Strings as well
    print("No")

print("\n")

# Example given in the Tutorial :-->
list1 = [1,2,3,4,5,6,7]
list2 = ["Red", "Green", "Blue"]
print(list1)
print(list2)

# List Index :~~>
''' Each item/element in a list has its own unique index. This index can be used to access any particular item from the list.
    The first item has index[0], second item has index[1], third item has index[2] and so on'''
# Example given in the tutorial :-->
colors = ["Red", "Green", "Blue", "Orange", "White"]
#          [0]     [1]     [2]      [3]      [4]      ~~>    "Index Number"
print(len(colors))     # As there are five elements in the list, therfore, the length of the variable(list) i.e. colors will be "5"