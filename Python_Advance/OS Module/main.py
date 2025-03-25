# In this part I will learn about OS Module of python.

'''The os module in Python is a built-in library that provides functions for interacting with the operating system.
   It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.'''
# The os module provides functions for opening, reading, and writing files etc.

import os

if not(os.path.exists("data")):
   os.mkdir("data")
for i in range(1,101):
   os.mkdir(f"data/Day{i}")


if not(os.path.exists("Date")):
    os.mkdir("Date")
for i in range(1,101):
    os.mkdir(f"Date/days{i}")