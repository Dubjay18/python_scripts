import os
import shutil

path =  input("Enter the name of the directory to be sorted :- ")
text = input("files to sort:-")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    print(text in filename)
    if text in filename:
        if os.path.exists(path+'/'+text):
            print("Path already exists")
            shutil.move(path+'/'+file,path+'/'+text+'/'+file)
        else:
            os.makedirs(path+'/'+text)
            print("Path created")
            shutil.move(path+'/'+file,path+'/'+text+'/'+file)