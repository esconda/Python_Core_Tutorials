# Author: Burak Dogancay
import sys
def reusePrimObjects():
  #An interesting thing to note which may help optimize your applications is that primitives are actually also
  #refcounted under the hood. Let's take a look at numbers; for all integers between -5 and 256, Python always reuses
  #the same object:
  #Note that the refcount increases, meaning that a and b reference the same underlying object when they refer to the
  #primitive
  a = 1
  print(sys.getrefcount(1))
  
  b = 1
  print(sys.getrefcount(1))
  
def effectsOfDelCommand():
  print("will be continued")
  
def main():
  reusePrimObjects()
  effectsOfDelCommand()
  

if __name__ == '__main__':
    main()