# In this part I will do "Exercise 2 Solution"
# Exercise :->
''''Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
Your program should use time module to get the current hour. Here is a sample program and documentation link for you:'''

# Exercise Solution :~~>
import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))
print(hour)

if(hour >= 0 and hour < 12):
  print("Good Morning Sir!")
elif(hour >= 12 and hour < 17):
  print("Good Afternoon sir!")
elif(hour >= 17 and hour < 0):
  print("Good Evening Sir!")