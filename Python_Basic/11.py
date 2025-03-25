# In this part I will learn about if-else statment

# These are the examples of if-else statement
apple_price = int(input("Enter the price of \"Apple\" :"))
budget = 250

if (apple_price <= budget):
    print("Alexa, Add 1 kg apple to the cart.")
else:                                                 # This space before the print function is called indentation.
    print("Alexa, Do not add apple to the cart")

print("\n")

a = int(input("Enter your age :"))
print("Your age is", a)

if(a>18):         # If the expression evaluates "True": Execute the block of code inside if statement. After execution return to the code out of the if......else block.
    print("You can drive")     
else:             # If the expression evaluates "False": Execute the block of code inside else statement. After execution return to the code out of the if......else block.
    print("You cannot drive")    

print("\n")    

# Conditional operators are : " >, <, >=, <=, ==, != "
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)