import os
# Author: Burak Dogancay


def joinPaths():
    firstPath = os.getcwd()
    secondPath = os.getlogin()
    pathName = os.path.join(firstPath, secondPath)
    print("Joined Path Direction : ", pathName)
    print("---------------------")


def getParentDir():
    parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))#absolute path
    print("Parent Directpry is :", parentDirectory)
    print("---------------------")


def pathCompManipulation():
    pathName = os.path.join(os.getcwd(), 'foo.txt')
    dirName = os.path.dirname(pathName)
    baseName = os.path.basename(pathName)
    splitedName = os.path.split(os.getcwd())
    splitedTxtName = os.path.splitext(os.path.basename(pathName))
    print("Path Name is :", pathName)
    print("Direction File Name is :", dirName)
    print("Base File Name is :", baseName)
    print("Splited File Name is :", splitedName)
    print("Splited Text File Name is :", splitedTxtName)
    print("---------------------")


def isPathExist():
    pathName = os.getcwd()
    if os.path.exists(pathName):
        print("File is Exist")
    else:
        print("File does not exist")
    print("---------------------")


def checkFileType():
    dirname = os.getcwd()
    isDir = os.path.isdir(dirname)
    print("Is Dir ? : ",isDir)
    
    # to check if the given path is a file
    filename = dirname + 'Os.Path.py'
    isFile = os.path.isfile(filename)
    print("Is File ? : ",isFile)
    
    
    # to check if the given path is symbolic link
    symlink = dirname + 'some_sym_link'
    isSymbolic = os.path.islink(symlink)
    print("Is Symbolic ? : ",isSymbolic)
    
    # to check if the given path is a mount point
    mount_path = '/home'
    isMount = os.path.ismount(mount_path)
    print("Is Mount ? : ",isMount)
    print("---------------------")


def main():

    # Join paths
    joinPaths()
    # ----------------

    # Get Parent Directory
    getParentDir()
    # ----------------

    # Path Component Manipulation
    pathCompManipulation()
    # ----------------

    # Is Path Exist
    isPathExist()
    # ----------------
    
    # checkFileType
    checkFileType()
    # ----------------


if __name__ == '__main__':
    main()
