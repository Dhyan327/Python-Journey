# In this part I will learn about range function 

for i in range(7):  # If we run range function with only one argument which here is [7] then the python interpreter will do as follow :--> range(0,7) 
    print(i)
print("\n")

for i in range(7):
    print(i + 1)
print('\n')

for i in range(2,20,2):    # Here, The python interpreter will start printing from 2 to 20 and will omit 2 value in between. But it will not include 12
    print(i)
print("\n")

for i in range(1, 101):    # If the Range will be more, than the terminal showing output will automatically cleared after certain numbers 
    print(i)