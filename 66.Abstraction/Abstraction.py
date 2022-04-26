# Author: Burak Dogancay

from abc import abstractmethod
from abc import ABCMeta
from re import X

class AbstractClass(object):
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def printSomething(self):
    pass
    # Can be left completely blank, or a base implementation can be provided
    # Note that ordinarily a blank interpretation implicitly returns `None`,
    # but by registering, this behaviour is no longer enforced.

class SubClass(AbstractClass):
  def printSomething(self):
    print("This function is called")
  
  def calculation(self,variable):
    x=variable*variable
    print("Squareroot of X is:",x)
  

def main():
 # Call sub class 
 subClass= SubClass()
 subClass.printSomething()
 subClass.calculation(5)
 
  

  

if __name__ == '__main__':
    main()