# Importing necessary modules
import os
import shutil

# Getting the directory path from user
path =  input("Enter the name of the directory to be sorted :- ")

# Getting all the files in the directory
files = os.listdir(path)

# Looping through each file in the directory
for file in files:
    # Splitting the filename and extension
    filename, extension = os.path.splitext(file)
    extension = extension[1:] # Removing the "." from the extension
    
    # Checking if a directory with the same extension exists
    if os.path.exists(path+'/'+extension):
        print("Path already exists")
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file) # If it exists, move the file to that directory
    else:
        os.makedirs(path+'/'+extension) # If it doesn't exist, create a new directory with that extension
        print("Path created")
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file) # Then move the file to that directory
