# In this part I will learn more Methods of File IO

"""Readline Method :~~>"""
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

f = open("Myfile.txt",'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line,type(line))
        break

print('\n')

f1 = open('Myfile2.txt','r')
i = 0
while True:
    i += 1
    line1 = f1.readline()
    if not line1:
        break
    m1 = line1.split(",")[0]
    m2 = line1.split(",")[1]
    m3 = line1.split(",")[2]
    print(f"Marks of Student{i} in Maths is : {m1}")
    print(f"Marks of Student{i} in Physics is : {m2}")
    print(f"Marks of Student{i} in Chemistry is : {m3}")
    print(line1)


"""Writeline Method :~~>"""
# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

f2 = open("Myfile3.txt",'w')
line2 = ['Hello\n','how\n','are\n','you?\n']
f2.writelines(line2)
f2.close()

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence.
# If you want to add newlines between the strings, you can use a loop to write each string separately: