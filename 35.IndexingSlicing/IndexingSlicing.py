# Author: Burak Dogancay

def basicSlicing():
   variable = "Burak Dogancay"
   print("--BASIC SLICING--")
   print("Last variable:", variable[-1])
   print("All variable:", variable[:])
   print("All variable 2:", variable[::])
   print("From index 4 to end:", variable[4:])
   print("From beginning to position 6:", variable[:4])
   print("From index 3 to 10:", variable[3:10])
   print("Every 2nd element:", variable[::2])
   print("From index 1, to index 4 (excluded), every 2nd element): ", variable[1:4:2])
   print("Beginning from start to last position:", variable[:-1])
   print("Beginning from start to last 2 variable position:", variable[:-2])
   print("From the last element to the end:", variable[-1:])
   print("From index 2 to None, in reverse order:", variable[3:1:-1])
   print("---------------------")
   
def reversingObject():
  s = 'reversing op!'
  print("--REVERSE OBJECT--")
  print("Normal",s)
  print("Reversed",s[::-1])
  print("---------------------")
  
def assignmentOp():
  
  myList = [1, 2, 3]
  myList[1:3] = [4, 5]
  print(myList)
  
  myList = [1, 2, 3, 4, 5]
  myList[1:4] = [4, 5, 6]
  print(myList)
  
  myList = [1, 2, 3]
  myList[:] = [7, 8, 9]
  print(myList)
  
  myList = [1, 2, 3]
  myList[-2:3] = [4, 5,6]
  print(myList)
  
def basicIndexing():
  arr = ['tb2', 'akinci', 'anka', 'aksungur']
  print("--BASIC INDEX OBJECT--")
  print(arr[0])
  print(arr[1])
  print(arr[2])
  print(arr[-1])
  print(arr[-2])
  print("---------------------")
    
def main():
  basicSlicing()
  reversingObject()
  assignmentOp()
  basicIndexing()
    

if __name__ == '__main__':
    main()