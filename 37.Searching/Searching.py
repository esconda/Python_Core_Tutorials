# Author: Burak Dogancay
def searchingElement():
  
  uavList = ["Akinci","Aksungur","Anka"]
  print("--LIST SEARCHING--")
  print("Searched element UavList : ","Anka" in uavList)
  print("Searched element UavList : ","Tb2" in uavList)
  print("---------------------")
  
  numTuple = (1,2,3,4,5)
  print("--TUPLE SEARCHING--")
  print("Searched element numTuple : ",1 in numTuple)
  print("Searched element numTuple : ",6 in numTuple)
  print("---------------------")
  
  stringVar = "All tutorials are good"
  print("--STRING SEARCHING--")
  print("Searched element String : ", "tutorials" in stringVar)
  print("Searched element String : ", "my" in stringVar)
  print("---------------------")
  
  setList = {(20,30),(40,50),(70,80)}
  print("--SET SEARCHING--")
  print("Searched element setList : ",(20,30) in setList)
  print("Searched element setList : ",10 in setList)
  print("---------------------")

def getIndexStr():
  #String Indexes
  astring = 'What is the best place'
  astring.index('l') # 4
  astring.rindex('l') # 20
  astring.find('l') # 4
  astring.rfind('l') # 20
  
def listIndex():
  alist = [10, 16, 26, 5, 2, 19, 105, 26]
  # search for 16 in the list
  alist.index(16) # 1
  alist[1] # 16
  alist.index(15)
  
def tupleIndex():
  atuple = (10, 16, 26, 5, 2, 19, 105, 26)
  atuple.index(26) # 2
  atuple[2] # 26
  atuple[7] # 26 - is also 26!
  
#WILL BE CONTINUED...

def main():
  searchingElement()
  getIndexStr()
  listIndex()
  tupleIndex()
  
  
    

if __name__ == '__main__':
    main()