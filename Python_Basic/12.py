# In this part I will learn about "Else-if or Elif" statement 

# Sometimes the programmer may want to evaluate more than one condition, This can be done using elif statement 

"""
--> Execute the block of code inside the if statement, if the initial expression evaluates to "True". After execution returns to the code out of the if block.
If not then,
--> Execute the block of code inside the first elif statement, if the expression inside it evaluate "True". After execution returns to the code out of the elif block.
If not then,
--> Execute the block of code inside the second elif statement, if the expression inside it evaluate "True". After execution returns to the code out of the elif block.
If not then,
"
"
--> Execute the block of code inside the nth elif statement, if the expression inside it evaluate "True". After execution returns to the code out of the elif block.

"""
num = int(input("Enter the number :"))

if (num < 0):
    print("The number is \"Negative\"")
elif (num == 0):
    print("The number is \"zero\"")
elif(num == 27 or num == 3):
    print("The number is \"special\"")
else:
    print("The number is \"Positive\"")

print('I am "Happy" now ')