# Author: Burak Dogancay
def powOp(num):
  return num * num

def averageOp(*args):
  return float(sum(args)) / len(args)

def mapExample():
  #Gets length of the list variables
  myList=['tb2','akinci','aksungur','anka']
  mapVar = list(map(len,myList))
  print("Map Variable : ", mapVar) 
  
def iterableMapping():
  #Lambda base operation for map
  mapVar = list(map(lambda x:x*2,[1,2,3,4,5,6,7]))
  print("Iterable Map Variable",mapVar)

def mapExample2():
  #run function with map variables
  myList = list(map(powOp,[2,3,4,5,6]))
  print("Pow Function of Map Variable",myList)

def mapExample3():
  #pass jultiple variable to function and define map with it
  var1 = [50,52,54,56]
  var2 = [42,40,41,46]
  var3 = [58,62,66]
  
  mapVarList = list(map(averageOp,var1,var2,var3))
  print("Multi map variable",mapVarList)
  
def mapExamples4():
  var1 = ['Akinci','Aksungur','Anka','Tb2']
  var2 = [42,40,41,46]
  var3 = [58,62,66]
  
  mapVarList = list(map(len,var1))
  print("Multi Map Variable2", mapVarList)
  
  

def main():
  mapExample()
  iterableMapping()
  mapExample2()
  mapExample3()
  mapExamples4()
  
    

if __name__ == '__main__':
    main()