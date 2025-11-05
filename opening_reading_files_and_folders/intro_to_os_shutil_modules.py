'''
- Python's os and shutil modules allows you to easily navigate files and directories on the computer and  then perform actions on them, such as moving them or deleting them. 
- os module is really usefull because it allows you to get the current working directory or list all the files in a directory
'''
import os, shutil
from send2trash import send2trash

# Let's open a practice.txt file since this files doesn't already exist so it will create a new one in the directory
'''f = open('practice.txt', 'w+')
f.write('This is just a template text to test things')
f.close()'''

# GETTING CURRENT WORKING DIRECTORY
'''
you can use os.getcwd() to get the current working directory or you can write pwd in your command line to check your current working directory but that has nothing do exclusively with python but it simply displays the current working directory in your command line so you can use that also but if you just want to see the directory, while this one will give access to the current working directory in any python script
'''
print(os.getcwd())

#LISTING DIRECTORIES AND FILES
'''
if you want to see the list of everything in a particular directory if you don't pass any argument 
it will return the list of contend for the current working directory 
'''
# print(os.listdir())
'''
now if I want to see all the files and folders on my desktop I can simpy pass the path to my desktop to list directory method of os module
'''
# print(os.listdir("C:\\Users\\sraan\\Desktop"))

#MOVING
'''
if you want to move any file or directory you can shutil modules move method, it accepts two arguments src which you want to move and the destination the place where you want to move it's path
'''
# shutil.move('practice.txt',  'C:\\Users\\sraan\\Desktop')

# DELETING FILES AND DIRECTORIES
'''
os.unlink(path)-> deletes a file at the path you provide
'''
# os. unlink('C:\\Users\\sraan\\Desktop\\Python_Course\\useless\\empty.txt')
# os. unlink('C:\\Users\\sraan\\Desktop\\Python_Course\\useless\\empty.py')

'''
os.rmdir(path)-> deletes a folder(folder must be empty) at the path you provide
'''
# os. rmdir('C:\\Users\\sraan\\Desktop\\Python_Course\\useless\\empty_folder')

'''
shutil.rmtree(path) DANGEROUS, as it will remove all files and folder at the path you provided
'''  
# shutil.rmtree("C:\\Users\\sraan\\Desktop\\Python_Course\\useless")
'''
(But always keep in mind all the three above mentioned methods permanently delete the files or folders so you can't even recover them from bin so always be cautious use them only if you are 100% sure that you never need them again)'''

# Using send2trash 
'''
Or else there's a better option of using third party send2trash library
install it using pip install send2trash
And then finally import send2trash method from send2trash package by using from send2trash import send2trash
'''
# send2trash("practice.txt")

# Using os.walk()
'''
os.walk is a directory tree generator that means for each directory in the directory tree rooted at top(including top itself, but excluding '.' and '..'), yeilds a 3-tuple dirpath, dirnames, filenames
'''
file_path = 'C:\\Users\\sraan\\Desktop\\Python_Course\\top_level_folder' 
for folder, sub_folders, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print("The subfolders are:")
    for sub_fold in sub_folders:
        print(f"subfolder: {sub_fold}")
    print("\n")
    print("The files are:")
    for file in files:
        print(f"file: {file}")
    print("\n")