from fileinput import filename
from inspect import getfile
import mmap
import os
from sympy import content
import shutil

#Author: Burak Dogancay

def getFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName

def fileModes():
    #'r' - reading mode. The default. It allows you only to read the file, not to modify it. When using this mode the file must exist.
    #'w' - writing mode. It will create a new file if it does not exist, otherwise will erase the file and allow you towrite to it.
    #'a' - append mode. It will write data to the end of the file. It does not erase the file, and the file must exist for this mode.
    #'rb' - reading mode in binary. This is similar to r except that the reading is forced in binary mode. This isalso a default choice.
    #'r+' - reading mode plus writing mode at the same time. This allows you to read and write into files at thesame time without having to use r and w.
    #'rb+' - reading and writing mode in binary. The same as r + except the data is in binary
    #'wb' - writing mode in binary. The same as w except the data is in binary.
    #'w+' - writing and reading mode. The exact same as r + but if the file does not exist, a new one is made.Otherwise, the file is overwritten.
    #'wb+' - writing and reading mode in binary mode. The same as w + but the data is in binary.
    #'ab' - appending in binary mode. Similar to a except that the data is in binary.
    #'a+' - appending and reading mode. Similar to w + as it will create a new file if the file does not exist.Otherwise, the file pointer is at the end of the file if it exists.
    #'ab+' - appending and reading mode in binary. The same as a + except that the data is in binary.
    try:
        with open(getFile('something.txt'),"r") as readFile:
            print("Files is available")
            print("---------------------")
            readFile.close()
    except FileExistsError:
        print("File can not be opened")
        
def readByLine():
    if os.path.isfile(getFile("something.txt")):
        #Read by line methode  
        with open(getFile("something.txt"),"r") as readFile:
            for line in readFile:
                print("Current Line : ",line)
            readFile.close()
        #---------------------
        
        #Read by Line alternative methode
        with open(getFile("something.txt"),"r") as readFileAlt:
            while True:
                currentLine = readFileAlt.readline()
                if currentLine== '':
                    break
                print("Current Line Alternative :",currentLine)
            readFileAlt.close()
        #---------------------
    print("---------------------")
    
def writingToFile():
    if os.path.isfile(getFile("something.txt")):
        with open(getFile("something.txt"),"w") as writeFile:
            writeFile.write("Mercedes ")
            writeFile.write("Bmw ")
            writeFile.write("Volskwagen ")
            writeFile.write("Toyota ")
            writeFile.write("Tesla ")
        writeFile.close()
    print("---------------------")
    
def iterateAllFiles():
    #To iterate all files, including in sub directories, use os.walk
    """ print("Directory folder : ",os.getcwd())
    for root, folders, files in os.walk(os.getcwd()):
        print ("Root : " , root)
        for filename in files:
            print("Files : ", filename) """
            
def fullContentFile():
    if os.path.isfile(getFile("something.txt")):
        with open(getFile("something.txt")) as readFile:
            contentFile = readFile.read()
            print("Content of a File : ",contentFile) 
            readFile.close()
    print("---------------------")
    
def randomFileAccess():
    if os.path.isfile(getFile("something.txt")):
        with open(getFile("something.txt"),'r+') as readFile:
            mmVar = mmap.mmap(readFile.fileno(), 0)
            print("Print Characters : ", mmVar[5:10])
            print("Print The Line Starting from current pos: ",mmVar.readline())
            print("Returning position to the beginnig of the file : ", mmVar.seek(0))
        print("---------------------")
        mmVar.close()    
        readFile.close()
    print("---------------------")
        
def copyDirectoryTree():
    print("Copy directory to destination")
    #source='//192.168.1.2/Daily Reports'
    #destination='D:\\Reports\\Today'
    #shutil.copytree(source, destination) # copy directory from src to dst
    #shutil.copyfile(src,dts) #copy file from src to dst
    print("---------------------")
    
def main():
    
    # Call File Modes
    fileModes()
    #----------------
    
    # Reading File By Name
    readByLine()
    #----------------
    
    #Iterate All Files
    iterateAllFiles()
    #----------------
    
    #Iterate All Files
    fullContentFile()
    #----------------
    
    #Write File
    writingToFile()
    #----------------
    
    #Random File Access
    randomFileAccess()
    #----------------
    
    #Copy Directory Tree
    copyDirectoryTree()
    #----------------


if __name__ == '__main__':
    main()
