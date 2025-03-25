# In this part I will learn about Nested-if statement 

# We can use if, if-else, elif statement inside other "If" statement as well like this :
# This is called "Nested-If"statements 

num = float(input("Enter the number :"))

if (num < 0):
    print("The number is \"Negative\"")

elif (num > 0):
    if (num <= 10):
        print("The number is between 1-10")
    elif(num > 10 and num <=20):
        print("The number is between 11-20")    
    elif(num > 20 and num <=50):
        print("The number is between 21-50")
    elif(num > 50 and num <=100):
        print("The number is between 50-100")
    elif(num > 100):
        print("The number is greater than 100")
else:
    print("The number is zero")