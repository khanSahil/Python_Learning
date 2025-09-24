f = open("practice.txt", "w+")
f.write("This is a test string")
f.close()

import os
print(os.getcwd())
print(os.listdir())
print(os.listdir("/home/sahkhan"))

import shutil

#shutil.move("practice.txt", "/home/sahkhan")

# Deleting files
import send2trash

print(os.listdir())
send2trash.send2trash("practice.txt")
print(os.listdir())

for folder, subfolder, file in os.walk("/home/sahkhan/Python_Learning/"):
    print(f'Currently looking at {folder}')
    print("\n")
    print(f'The subfolders are: ')
    for sub_fold in subfolder:
        print(f'Subfolder: {sub_fold}')
    
    print('\n')
    print("the files are: ")
    for f in file:
        print(f'File: {f}')
    print('\n')