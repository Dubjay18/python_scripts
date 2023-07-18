import os
import shutil

path =  input("Enter the name of the directory to be sorted :- ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(path+'/'+extension):
        print("Path already exists")
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        print("Path created")
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)