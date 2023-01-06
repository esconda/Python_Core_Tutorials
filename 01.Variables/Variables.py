import os
#Author: Burak Dogancay

def dataTypes():
    #float
    floatVar = 10.4
    #---------------

    #int
    intVar = 20
    #----------
    
    #boolean type
    boolVar = True
    #-------------

    #string
    string = "my string"
    string_length = len(string)
    #--------------------------
    
    #SequenceTypes
    myList = list()
    myRange = range
    myTuple = tuple()
    #--------------------------
    
    #MappingType
    myDict = dict()
    #--------------------------
    
    #SetTypes
    mySet = set()
    #--------------------------
    
    #BinaryTypes
    rList = [1, 2, 3, 4, 5]
    myBytes = bytes(rList)
    myByteArray = bytearray(rList)
    myMemView = memoryview(myBytes)
    #--------------------------


    print("Float variable :" , type(floatVar))
    print("Int variable :" , type(intVar))
    print("Bool variable :" , type(boolVar))
    print("String Variable : ", type(string))
    print("List variable :" , type(myList))
    print("Range variable :" , type(myRange))
    print("Tuple Variable : ", type(myTuple))
    print("Dict Variable : ", type(myDict))
    print("Set Variable : ", type(mySet))
    print("Bytes Variable : ", type(myBytes))
    print("Byte Array Variable : ", type(myByteArray))
    print("MemView Variable : ", type(myMemView))
    
    print("String Length : ", string_length)
    print("Part of string : ", string[0:6])
    
def main():
    dataTypes()
  


if __name__=='__main__':
    main()