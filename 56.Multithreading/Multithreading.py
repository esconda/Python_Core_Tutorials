# Author: Burak Dogancay
import threading
import time
from random import randint


def firstFunc():
  uavList = ['tb2','anka','aksungur', 'akinci','MQ1-PREDATOR']
  
  for uav in uavList[0:4]:
    time.sleep(randint(1,2)) #wait for 1 or 2 second
    print("Uav type is : ", uav) #get uav
    print("--------------")

def secondFunc():
  ugvList = ['pars','kaplan','ejder']
  
  for ugv in ugvList:
    time.sleep(randint(1,2)) #wait for 1 or 2 second
    print("Ugv type is : ", ugv) #get ugv
    print("--------------")


def main():
 #strating thread
 #Start function with thread
 firstThread = threading.Thread(target=firstFunc)
 secondThread = threading.Thread(target=secondFunc)
 
 firstThread.start()
 secondThread.start()
 #---------------------------


if __name__ == '__main__':
    main()