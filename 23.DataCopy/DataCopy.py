#Author: Burak Dogancay
import copy
def copyDict():
    #It performs a shallow copy of the dictionary.
    myDict = {"uav1": "TB2", "uav2": "Akıncı", "uav3":"Anka"}
    myDictCpy = myDict.copy()
    myDict["uav4"] = "Aksungur"
    
    print("COPY DICTIONARY")
    print(" First dict : ", myDict)
    print(" Second dict : ", myDictCpy)
    print("---------------------")
    
def deepCpyList():
    #It performs a deep copy of the List.
    myList = ["TB2","AKINCI"]
    myListDeepCpy = copy.deepcopy(myList)
    myList.append("Aksungur")
    
    print("DEEP COPY LIST")
    print(" First List : ", myList)
    print(" Second List : ", myListDeepCpy)
    print("---------------------")
    
def shallowCpyList():
    #It performs a shallow copy of the List.
    myList = ["TB2","AKINCI"]
    myListShallowCpy = myList[:]
    
    print("SHALLOW COPY LIST")
    print(" First List : ", myList)
    print(" Second List : ", myListShallowCpy)
    print("---------------------")
    
def cpySet():
    #It performs a shallow copy of the Set.
    myList = {("TB2","AKINCI")}
    myListShallowCpy = myList.copy()
    
    print("SHALLOW COPY SET")
    print(" First Set : ", myList)
    print(" Second Set : ", myListShallowCpy)
    print("---------------------")
    
def main():
  copyDict()
  deepCpyList()
  shallowCpyList()
  cpySet()
    

if __name__ == '__main__':
    main()
