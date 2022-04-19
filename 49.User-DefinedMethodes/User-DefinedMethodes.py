# Author: Burak Dogancay
""" User-defined method objects may be created when getting an attribute of a class (perhaps via an instance of that
class), if that attribute is a user-defined function object, an unbound user-defined method object, or a class method
object. """
class A(object):
  # func: A user-defined function object
  #
  # Note that func is a function object when it's defined,
  # and an unbound method object when it's retrieved.
  def func(self):
    pass
    # classMethod: A class method
  @classmethod
  def classMethod(self):
    pass
  
class B(object):
  # unboundMeth: A unbound user-defined method object
  #
  # Parent.func is an unbound user-defined method object here,
  # because it's retrieved.
  unboundMeth = A.func
  
def overrideMethod():
  a = A()
  b = B()
  print("--User Defined Methodes--")
  print (A.func)
  # output: <unbound method A.func>
  print (a.func)
  # output: <bound method A.func of <__main__.A object at 0x10e9ab910>>
  print (B.unboundMeth)
  # output: <unbound method A.func>
  print (b.unboundMeth)
  # output: <unbound method A.func>
  print (A.classMethod)
  # output: <bound method type.classMethod of <class '__main__.A'>>
  print (a.classMethod)
  # output: <bound method type.classMethod of <class '__main__.A'>>
  print("---------------------")
  
def main():
  overrideMethod()


if __name__ == '__main__':
    main()