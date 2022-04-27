# Author: Burak Dogancay
import threading
import time
import multiprocessing
from tracemalloc import start


def fib(n):
  """computing the Fibonacci in an inefficient way
  was chosen to slow down the CPU."""
  print("Calculate fibonacci")
  if n <= 2:
    return 1
  else:
    return fib(n-1)+fib(n-2)

def main():
 #Using MultiProcessing
 poolProcessing = multiprocessing.Pool()
 print(poolProcessing.map(fib,[12,11,10,9,8]))
#-----------------------

if __name__ == '__main__':
    main()