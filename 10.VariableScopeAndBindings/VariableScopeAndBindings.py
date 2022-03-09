from enum import Enum
#Author: Burak Dogancay
globalVariable = 20 #Global Variable

def main():

    #Global Variable
    global globalVarAlternative
    globalVarAlternative = 50
    print("Global Variable : ", globalVariable)
    print("Global Variable Alternative : ", globalVarAlternative)

    #The Del Command
    #Note that del is a binding occurrence, which means that unless explicitly stated otherwise (using nonlocal
    #or global), del v will make v local to the current scope. If you intend to delete v in an outer scope, use
    #nonlocal v or global v in the same scope of the del v statement.
    x = 5
    print(x)
    # del x
    # print(x) # gives error

    #Global and local variables
    specificGlobVar = [a for a in globals().keys() if a =='globalVariable']
    print(specificGlobVar)
    print(globals().keys())
    print(locals().keys())


if __name__=='__main__':
    main()