# In this part I will learn about "Do While Loop"
''' Do- while is a loop in which a set of instruction will execute atleast once(irrespective of the condition)
and then the repetition of loop's body will depend on the condition passed at the end of the while loop'''
# This Loop is also known as "Exit- Controlled Loop" 
# :~~> To create a do while loop in python, you need to modify the while loop a bit in order to get similar behavior to a "Do While Loop"
''' :~~> The most common technique to emulate a 'do while loop' in python is to use an infinite while loop 
with a break statement wrapped in an if statement that checks the condition and breaks the iterationif that condition become true.''' 
# we can emulate the Do While Loop by "Infinite While Loop"
# This is the syntax of Do While Loop, [The following syntax does not work for python but it works for other programming languages such as c, java, c++ etc]
'''
do {
    loop body;
} while(condition);
'''

# Example :-->
i = 0
while True:         # Here if we write "true" instead of "True" with capital 'T' then it will give error 
    print(i)
    i = i + 1
    if(i%100 == 0):
        break

# Example given in the tutorial :-->
while True:
    number =  int(input("Enter a positive number :"))
    print(number)
    if not number > 0:     # It means that {if number < 0:}
        break
print("Done with the loop")