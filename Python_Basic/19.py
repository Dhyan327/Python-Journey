# In this part I will learn about "Break" statement 
# Break statement enables a program to skip over a part of code. A break statement terminates the very loop it lies within.

# Break means "Leaving from the loop"
# Examples :-->
for i in range(1,17):       
    print("5 X",i,"=",5*i)
    if (i == 10):
        break
print("\n")

# We can also run the above code similarly in the following manner 
for i in range(17):
    if(i == 10):
        break
    print("5 X",i+1,"=",5*(i+1))
print("\n")

# Example given in tutorial :-->
for i in  range(1,101,1):
    print(i, end="__ \n")
    if(i == 20):
        break
    else:
        print('Mission python')
print("Thank you")
print("\n")

# We can also take the input from the user in range. The following is the example of this 
for x in range(int(input("Enter the number :"))):      
    print("3 X",x+1,"=",3*(x+1))
    if ((x+1)%10 == 0): 
        print("\n")