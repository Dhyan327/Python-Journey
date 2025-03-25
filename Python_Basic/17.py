# In this part I will learn about "While Loop"
# As the name suggest, While loops execute statements while the condition is "True". As soon as the condition becomes "False", the intepreter comes out of the while loop.

# Example :-->  [Incrementing loop]
i = 0
while i <= 7:
    print(i)                      
    i = i + 1
else:                              # Doing "While Loop" with else statement
    print("Done with the Loop")
print("\n")

# Example  :--> [Decrementing loop]
count = int(input("Enter the number :"))
if(count > 0):
    while (count >= 0):
        print(count)               # Doing "While Loop" with if-else statement
        count = count - 1         
else:
    print("The number is", count)
print("\n")

# Example :-->
while  True:
    x = int(input("Enter the number :"))
    if x <= 327:
        print(x)
    else:
        break
print("Done with the loop")