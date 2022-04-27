# Author: Burak Dogancay
import multiprocessing
import time
from unittest import result
import Multiprocessing
from random import randint
from multiprocessing import Pool

def firstProcess():
  uavList = ['tb2','anka','aksungur', 'akinci','MQ1-PREDATOR']
  
  for uav in uavList[0:4]:
    time.sleep(randint(1,2)) #wait for 1 or 2 second
    print("Uav type is : ", uav) #get uav
    print("--------------")

def secondProcess():
  ugvList = ['pars','kaplan','ejder']
  
  for ugv in ugvList:
    time.sleep(randint(1,2)) #wait for 1 or 2 second
    print("Ugv type is : ", ugv) #get ugv
    print("--------------")

def thirdProcess(pList):
  for element in pList:
    time.sleep(randint(1,2)) #wait for 1 or 2 second
    print(" Element is : ",element) #get ugv
    print("--------------")

def main():
  #Multiprocessing
  workerProcess1 = multiprocessing.Process(target=firstProcess)
  workerProcess2 = multiprocessing.Process(target=secondProcess)
  
  #startWorkers
  workerProcess1.start()
  workerProcess2.start()
  
  #Join workers this will block parent main process
  #until the workes are complete
  workerProcess1.join()
  workerProcess2.join()
  
  #USING POOL MAP
  myList = ['One','Two']
  pool = Pool(3) #Create 3 times of process 
  pool.map(thirdProcess,myList)
  #----------------------
  
  #this loop will be blocked until all multiprocessing process are finished
  for i in range(30):
    print(i)
    
  #ALL process are finished
  print("ALL PROCESS ARE FINISHED")
  
if __name__ == '__main__':
    main()