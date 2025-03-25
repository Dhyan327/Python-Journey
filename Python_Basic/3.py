# In this part I will learn about types of type casting i.e. Explicit and Implicit

# The conversion of one datatype into another datatype, done via programmer intervention or manually as per the requirement is called "Explicit Typecasting"
# This is an example of Explicit TypeCasting
string = "15"
number = 7
print("The sum of the two number is",int(string) + number) 

# OR :-->

string_number = int(string)      # It throws an error if string is not an valid integer 
sum = string_number + number
print("The sum of the numbers is :", sum)

# This is an example of Implicit TypeCasting  

c = 2.9
d = 7     
print("The Sum is :",c + d )

'''
 Here one variable has float value while another has integer value 
 so, The sum of both variable will convert in a float value directly by the python interpreter 
 So one data type is converted into another datatype by python interpreter itself.
 Hence, it is called Implicit TypeCasting
'''