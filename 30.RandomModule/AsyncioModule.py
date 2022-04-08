# Author: Burak Dogancay
import random
from string import punctuation, ascii_letters, digits

def randomUserPass():
    #Create Random  Password
    symbolsStr = ascii_letters +punctuation+digits
    secureRandom= random.SystemRandom()
    password = "".join(secureRandom.choice(symbolsStr) for i in range(10))
    print("--RANDOM PASSWORD--")
    print(password)
    print("---------------------")

def randValFromList():
    myList=[1,2,3,4,5,6]
    randVal=random.choice(myList)
    print("--RANDOM VAL FROM LIST--")
    print(randVal)
    print("---------------------")

    
def main():
    randomUserPass()
    randValFromList()
   
    

if __name__ == '__main__':
    main()