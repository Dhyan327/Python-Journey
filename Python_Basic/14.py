# In this part I will learn about Match Case statement 
# Match case statements is similar to the switch statement of C, C++ etc.

# Example :-->
x = int(input("Enter the value of X :"))              # X is the variable to match

match x:
    case 0:     # If x is "0"
        print("x is \"Zero\"")
# Case with if condition
    case 4  if x % 2 == 0:    # While putting if condition in case we have to remember that we don't to put colon (:) after using case function 
        print("Case is 4") 
# Empty case with if condition 
    case _ if x < 10 :         # Default case (Will only be matched if the above cases were not matched). So, It is basically an else statement 
        print("X is less than 10")
    case _ :
        print("The number is ", x)