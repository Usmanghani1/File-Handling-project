from pathlib import Path
import os

def createfile():
    try:
        name = input("Please enter your file name:- ")
        path = Path(name)
        if not path.exists():
            with open(path, "w") as fs:
                data = input(f"please write what you want to wite in your {name} file:-")
                fs.write(data)
            print(f"your file {name} has been created successfully:- ")
        else:
            print("Error file name is aleady exists:- ")
    except Exception as err:
        print(f"Error accurd as {err}")

def readfile():
    try:
        name = input("please enter your file name:- ")
        path = Path(name)
        if path.exists():
            with open(path, "r") as fs:
                content = fs.read()
            print(f"your content is:-\n {content}")
        else:
            print("Error File name is not exists:- ")
    except Exception as err:
        print(f'Error accurd as {err}')    

def appendfile():

    try:
        name = input("Please enter the file name:- ")
        path = Path(name)
        if path.exists():
            print("--:options:--")
            print("please enter 1 to rename the file:- ")
            print("please enter 2 to append the file:- ")
            print("please enter 3 to overwrite the file:- ")
            choice = int(input("please enter your choice:- "))

            if choice == 1:
                newname = input("Please enter your file's new name:- ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print(f"Your file name has been changed successfully:- ")
                else: 
                    print("Error Name is already exists:- ")

            if choice == 2:
                with open(path, "a") as fs:
                    data  = input("Please write what you want to append:- ")
                    fs.write(data)
                print("you append your file successfully:- ")

            if choice == 3:
                with open(path, "w") as fs:
                    data = input("please write what you want to write:- ")
                    fs.write( data)
                print("your file is overwrite successfully:- ")
    except Exception as err:
        print(f"Error accurd as {err}")

def deletefile():
    try:
        name = input("please tell the file name:- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("your file is deleted successfully:- ")
        else:
            print("Error file name doesn't exists:-")
    except Exception as err:
        print(f"Error accurd as {err}")

print("Pease type 1 to create a new file:- ")
print("Pease type 2 to read file:- ")
print("Pease type 3 to append file:- ")
print("Pease type 4 to delete file:- ")

a = int(input("please enter your option:- "))

if a == 1:
    createfile()
elif a == 2:
    readfile()
elif a == 3:
    appendfile()
elif a == 4:
    deletefile()