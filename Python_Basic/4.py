# In this part I will learn about "Taking input from the user"

a = input("Enter your name :")    # When we take user input directly by using input() function , The input function returns the value as string.
print("Your name is ",a)       # If we want to take numeric value from user then we have to typecast them whenever required to another datatype. 

x = float(input("Enter your first number :"))           # Here the first option is to directly write the float function along with taking the user's input
y = float(input("Enter the second number :"))
print("The sum of the two number is :",x + y)

c = input("Enter your first number :")          # The second option is with TypeCasting. 
d = input("Enter the second number :")          # Here, we have to declar that the value in the variable is integer or float while writing print function
print("The product of the two number is :",int(c) * int(d)) 