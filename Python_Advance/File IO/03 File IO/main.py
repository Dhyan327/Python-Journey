# In this part I will learn more Methods of File IO

"""Seek Method :~~>"""
# The seek() function allows you to move the current position within a file to a specific point. 
# The position is specified in bytes, and you can move either forward or backward from the current position.

with open('File.txt', 'r') as f:
    print(type(f))
    f.seek(13)          # Move to the 13th byte in the file
    data = f.read(7)    # Read the next 7 bytes
    print(data)
print(" ")

"""Tell Method :~~>"""
# The tell() function returns the current position within the file, in bytes.
# This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position.

with open("Myfile.txt",'r') as x:
    x.seek(7)
    print(x.tell())
    data1 = x.read(8)
    print(data1)
    print(x.tell())
print(" ")

"""Truncate Method :~~>"""
# When you open a file in Python using the open function, you can specify the mode in which you want to open the file. 
# If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. 
# However, if you want to truncate the file to a specific size, you can use the truncate function.

with open('Sample.txt', 'w') as z:
  z.write('Hello World!')
  z.truncate(5)

with open('Sample.txt', 'r') as y:
  print(y.read())