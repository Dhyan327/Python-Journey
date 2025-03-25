# In this part I will do "Exercise 7 Solution"
# Exercise :->
""" Write a program to clear the clutter inside a folder on your computer.
    You should use OS module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder.
    Do the same for other file formats. """

# Solution :~~>
import os

files = os.listdir()
i = 1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"{file}",f"{i}.jpg")
        i = i + 1

# Note :~~>
""" Here, it will raise error if the file name is already existed and also note to open the folder in separate window. """