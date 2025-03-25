import os
folders = os.listdir("Date")
print(folders)

print(os.getcwd())

for i in folders:
    print(i)
    print(os.listdir(f"Date/{i}")) 