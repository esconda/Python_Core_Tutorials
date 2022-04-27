# Author: Burak Dogancay
import threading
import time
import multiprocessing
from tracemalloc import start

#In the latter case, multiprocessing can be effective as multiple processes can, of course, execute multiple instructions simultaneously.Multiprocess option works better and faster than threading option
def function():
  for i in range(100000):
    x = i+1
    x2 = x*5

def main():
  #One run of the function
  startTime = time.time()
  function()
  print("One run took : ", (time.time() - startTime))
  
  #Multi threading example
  startTime = time.time()
  threads = [threading.Thread(target=function) for _ in range(4)]
  for t in threads:
    t.start()
  for t in threads:
    t.join()
  print("4 threading took : ", (time.time() - startTime))
  #-----------------------------
  
  #MultiProcessing Example
  startTime = time.time()
  processes = [multiprocessing.Process(target=function) for _ in range(4)]
  for p in processes:
    p.start()
  for p in processes:
    p.join()
  print("4 process took : ",(time.time() - startTime))
  #-----------------------------
  
  #THREAD LOCK
  #lock = threading.Lock()
  
  #PROCESS LOCK
  #lock = multiprocessing.Lock()

if __name__ == '__main__':
    main()