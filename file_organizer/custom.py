# Importing necessary modules
import os
import shutil

# Getting the directory path and file name from user
path =  input("Enter the name of the directory to be sorted: ")
text = input("Enter the name of the file to sort: ")
files = os.listdir(path)

# Looping through each file in the directory
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:] # Removing the "." from the extension
    
    # Checking if the file name contains the text to sort
    if text in filename:
        # Checking if a directory with the same name as text exists
        if os.path.exists(path+'/'+text):
            print("Path already exists")
            shutil.move(path+'/'+file, path+'/'+text+'/'+file) # If it exists, move the file to that directory
        else:
            os.makedirs(path+'/'+text) # If it doesn't exist, create a new directory with that name
            print("Path created")
            shutil.move(path+'/'+file, path+'/'+text+'/'+file) # Then move the file to that directory
