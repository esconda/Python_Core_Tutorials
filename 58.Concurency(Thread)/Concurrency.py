# Author: Burak Dogancay
import threading
import time
import multiprocessing
from tracemalloc import start


def countUp(count):
  while count < 50:
    print("Count Type: ", count)
    count += 1
  return

def main():
  #Multiprocessing Module
  #Here, each function is executed in a new process. Since a new instance of Python VM is running the code, there is
  #no GIL and you get parallelism running on multiple cores.
  #The Process.start method launches this new process and run the function passed in the target argument with
  #the arguments args. The Process.join method waits for the end of the execution of processes p1 and p2.
  
  #*If you use a Lock in MainThread and pass it to another thread which is supposed to lock it at some point. If
  #the fork occurs simultaneously, the new process will start with a locked lock which will never be released as
  #the second thread does not exist in this new process.
  firstProcess = multiprocessing.Process(target=countUp, args=(10,))
  firstProcess.start()
  
  secondProcess = multiprocessing.Process(target=countUp, args=(20,))
  secondProcess.start()
  
  firstProcess.join()
  secondProcess.join()
  ##----------------------
  
  #Threading Module
  firstThread = threading.Thread(target=countUp,args=(10,))
  firstThread.start()
  secondThread = threading.Thread(target=countUp,args=(20,))
  secondThread.start()
  #-----------------------

if __name__ == '__main__':
    main()