# Author: Burak Dogancay
import random
from string import punctuation, ascii_letters, digits

from torch import rand

def randomUserPass():
    #Create Random  Password
    symbolsStr = ascii_letters +punctuation+digits
    secureRandom= random.SystemRandom()
    password = "".join(secureRandom.choice(symbolsStr) for i in range(10))
    print("--RANDOM PASSWORD--")
    print(password)
    print("---------------------")

def randValFromContainers():
    myList=[1,2,3,4,5,6]
    myTuble=(20,30,40,50)
    
    randValList=random.choice(myList)
    randValTuple=random.choice(myTuble)
    print("--RANDOM VAL FROM CONTAINER--")
    print("Random Value from list : ",randValList)
    print("Random Value from tuple",randValTuple)
    print("---------------------")

def shuffleList():
    myList=[1,2,3,4,5,6]
    random.shuffle(myList)
    print("--RANDOM LIST--")
    print("Random List:",myList)
    print("---------------------")

def randomVals():
    intVal=random.randint(5,15)
    floatVal=random.random()
    print("--RANDOM VARIABLES--")
    print("Random Integer : ",intVal)
    print("Random Float : ",floatVal)
    print("---------------------")

def otherFunctions():
    UAVS = ["Tb2","Akıncı","Anka","Aksungur"]
    #shuffling
    random.shuffle(UAVS)
    
    #Choice , takes random element form sequence
    oneRandVal = random.choice(UAVS)
    
    #Sample ,takes random many element form sequence
    manyRandVal=random.sample(UAVS,3)
    
    #Random Vals
    randVal = random.randrange(10,50)
    
    print("--RANDOM VARIABLES--")
    print("Shuffle List : ",UAVS)
    print("Random One Val : ",oneRandVal)
    print("Random Many Val : ",manyRandVal)
    print("Random Val : ",randVal)
    print("---------------------")
    
    
def main():
    randomUserPass()
    randValFromContainers()
    shuffleList()
    randomVals()
    otherFunctions()
    

if __name__ == '__main__':
    main()