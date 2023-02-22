#!/usr/bin/env python3
import os
import shutil

#get current working directory
dir_path = os.getcwd()
print("current working directory", dir_path)

#Takes the name of a file/folder as parameters and returns a value indicating the inode type
def getInodeType(name):
    if os.path.isdir(name):
        return "Directory"
    else:
        return "File"
    
def createFiles(dirName, M, ext):
    #create files under the current directory with a loop of M 
    for o in range(M):
        fName = "file_" + str(o+1) + ext
        open(fName, 'w')
        #Setting file permissions
        os.chmod(fName, 0o740)
def createSubDirectories(N, subDirCount):
    #create directories under the current directory with a loop of N
    for i in range(N):
        subDir = "dir_" + str(i+1)
        os.mkdir(subDir)
    
def renameFiles(dir_path,ext, new_ext):
    #Rename all files ending in .xls to .docx
    for file in os.listdir(dir_path):
        if getInodeType(file) == "File":
            os.rename(str(file), str(file).split(".")[0] + new_ext)

#Store entires in Lab3 directory in a dictionary with the file name as the key and file type as the value

#displaying the directory contents
def listEntries(name):
    print("Name \t\t\t\t\t Type")
    print("---- \t\t\t\t\t ----")
    for i in os.listdir(name):
        if getInodeType(i) == "Directory":
            print("{}\t\t\t\t\t {}".format(i, "Directory"))
        if getInodeType(i) == "File":
            print("{}\t\t\t\t {}".format(i, "File"))
    storedEntries = {}
    for file in os.listdir(dir_path + '\lab3'):
        if getInodeType(file) == "File":
            split = os.path.splitext(str(file))
            print(split)
            
    print(storedEntries)
    
    

def main():
    #Print the name of your current directory in the console
    print("current working directory", dir_path)
    
    l3 = dir_path + '\lab3'
    #Under working directory, create a new directory called Lab3
    #create an if statement to check if the directory exists
    if os.path.exists(l3):
        shutil.rmtree(l3)
    os.mkdir(l3)

    #change working directory to Lab3
    os.chdir(l3)

    #print the name of your current directory in the console
    print("current working directory:", os.getcwd())

    #Prompt to enter a positive number for M
    print("How many files do you want to create? (Only enter a number greater than or equal to 1)\n")
    M = int(input())
    while M <= 0:
        print("Please enter a number greater than or equal to 1")
        M = int(input())

    createFiles(l3, M, ".xls")
    #Prompt to enter a positive number for N
    print("How many directories do you want to create? (Only enter a number greater than or equal to 1)\n")
    N = int(input())
    while N <= 0:
        print("Please enter a number greater than or equal to 1")
        N = int(input())

    createSubDirectories(N,l3)
    renameFiles(l3, '.xls', '.docx')
    listEntries(l3)
main()