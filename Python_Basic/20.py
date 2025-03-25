# In this part I will learn about "Continue" statement
# The continue statement skips the rest of the loop statementts and causes the next iteration to occur 

# Continue means "Leaving the particular Iteration"
for i in range(20):
    if(i+1 == 1):
        print("Skip the interation")     # So, instead of the 10th iteration it will display "Skip the iteration"
        continue
    print("5 X",i+1,"=",5*(i+1))
print("\n")

# Example given in tutorial 
for x in [2,3,4,5,6,7,8,9]:
    if (x%2 != 0):
        print("Skip the iteration")
        continue
    print(x, end="__\n")