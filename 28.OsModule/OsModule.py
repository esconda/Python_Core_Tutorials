# Author: Burak Dogancay
import os
import locale

def getFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))  # it gets the folder location
    # add file name to folder location
    fileName = os.path.join(location, pFileName)
    return fileName

def getCurrentDir():
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return location

def getParentDirectory():
    parentDir = os.getcwd();
    print("--PARENT DIRECTORY--")
    print(parentDir)
    print("---------------------")

def createDirectory():
    #Create directory in current folder
    try:
        os.makedirs(getCurrentDir() + "/subdir2")
    except OSError:
        if not os.path.isdir(getCurrentDir() + "/subdir2"):
            raise
        
def createAnotherDir():
    #First methode to create directory
    try:
        os.mkdir(getCurrentDir() + "/subdir3")
    except OSError:
        if not os.path.isdir(getCurrentDir() + "/subdir3"):
            raise
        
    #Permision specific Methode to create directory
    try:
        os.mkdir((getCurrentDir() + "/subdir4"),mode=700)
    except OSError:
        if not os.path.isdir(getCurrentDir() + "/subdir4"):
            raise

def chkOpSystem():
    #Check Operating System
    opSystem = os.name
    print("-- OPERATING SYSTEM--")
    print(opSystem.capitalize())
    print("---------------------")
    
def removeDirectory():
    #Remove Directory from folder
    try:
        os.removedirs(getCurrentDir() + "/subdir2")
    except OSError:
        if not os.path.isdir(getCurrentDir() + "/subdir2"):
            raise
def changePermission():
    os.chmod(getCurrentDir(),mode=700)
    
def main():
    getParentDirectory()
    createDirectory()
    createAnotherDir()
    chkOpSystem()
    removeDirectory()
    changePermission()
    

if __name__ == '__main__':
    main()