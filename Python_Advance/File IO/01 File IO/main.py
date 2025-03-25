# In this part I will learn about File IO in python

"""Opening a File :-->"""

# Python provides the open() function to open a file.
# It takes two arguments: the name of the file and the mode in which the file should be opened.

"""Modes in file :~~>"""
# There are various modes in which we can open files.

# read (r)   : This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
# write (w)  : This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a) : This mode opens the file for appending only and creates a new file if the file does not exist.
# create (x) : This mode creates a file and gives an error if the file already exists.
# text (t)   : Apart from these modes we also need to specify how the file must be handled. Text mode is used to handle text files. t refers to the text mode.
#              There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
# binary (b) : This mode is used to handle binary files (images, pdfs, etc).

# f = open('Myfile.txt','r')
# content = f.read()
# print(content)
# f.close()

f = open('Myfile.txt' ,'r')
content = f.read()
print(content)
f.close()