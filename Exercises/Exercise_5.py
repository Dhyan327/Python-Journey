# In this part I will do "Exercise 5 Solution"
# Exercise :->
'''Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun.
   The gun beats the snake, the water beats the gun, and the snake beats the water.
   Write a python program to create a Snake Water Gun game in Python using if-else statements. Use proper functions to check for win.
'''

# Solution :->

import random

print("Welcome to Snake, Water and Gun Game!!")
print("\n")

i = 0
user_point = 0
comp_point = 0

while i < 5:
    a = input("Snake, Water or Gun : ").capitalize()
    b = random.choice(["Snake", "Water", "Gun"])

    print("You :~~>", a)
    print("Computer :~~>", b)

    a = a.capitalize()
    b = b.capitalize()

    if a == b:
        print("Round Draw!!!")

    elif (a == "Snake" and b == "Water") or (a == "Water" and b == "Gun") or (a == "Gun" and b == "Snake"):
        print("You win!!")
        user_point += 1

    else:
        print("Computer wins!!")
        comp_point += 1

    print("")

    i = i + 1

print("Your Point :~~>", user_point)
print("Computer Point :~~>", comp_point)
print("\n")

if user_point > comp_point:
    print("Congratulation! You Won!!")
elif user_point < comp_point:
    print("Oh! Sorry, You lose!! Better Luck Next Time!!")
else:
    print("Game Draw!!")
