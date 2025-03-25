# In this part I will learn about "Loop with Else Statement"
# As you have learned before, the else clause is used along with the if statement.
'''Python allows the else keyword to be used with the for and while loops too.
~~> The else block appears after the body of the loop.
~~> The statements in the else block will be executed after all iterations are completed.
~~> The program exits the loop only after the else block is executed.'''
# Syntax :-->
'''for counter in sequence:'''
        #Statements inside for loop block
'''else:'''
        #Statements inside else block

# Example :-->  [With "For Loop"]
for a in range(7):
    print(a)
else:
    print("Done with the loop")
print("\n")

# Example :-->  [With "For Loop" and "Break" Statement]
for b in range(7):
    print(b)
    if b == 3:
        break
else:               # Here, The 'Else Statement' will not be executed because the break statement will break the whole loop
    print("Done with the ioop")
print("\n")

# Example :-->  [With "While Loop"]
i = 0
while i < 7:
    print(i)
    i = i +1
else:
    print("Done with the loop")
print("\n")

# Example :-->  [With "While Loop" and "Break" Statement]
x = 0
while x < 7:
    print(x)
    x = x +1
    if x == 5:
        break
else:
    print("Done with the loop")
print("\n")

# '''Example given in Tutorial''' :-->
for d in range(7):
    print ("Iteration no. {} in for loop".format(d+1))
else:
    print ("Done with the loop")
print("\n")
print ("Out of loop")