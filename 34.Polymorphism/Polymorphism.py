# Author: Burak Dogancay
""" Polymorphism without inheritance in the form of duck typing as available in Python due to its dynamic typing
system. This means that as long as the classes contain the same methods the Python interpreter does not
distinguish between them, as the only checking of the calls occurs at run-time. """
class UAV:
  def motor(self):
    print("UAV Component is : Motor ")
  def camera(self):
    print("UAV Component is : Camera ")
  def wing(self):
    print("UAV Component is : Wing")
  def controller(self):
    print("UAV Component is : Controller")

class UGV:
  def motor(self):
    print("UGV Component is : Motor ")
  def camera(self):
    print("UGV Component is : Camera ")
  def launcher(self):
    print("UGV Component is : Launcher ")
    
def robots(obj):
  obj.motor()
  obj.camera()
  
#BASIC POLYMORPHISM
#Polymorphism is the ability to perform an action on an object regardless of its type. This is generally implemented
#by creating a base class and having two or more subclasses that all implement methods with the same signature.
#Any other function or method that manipulates these objects can call the same methods regardless of which type
#of object it is operating on, without needing to do a type check first.
#In object-oriented terminology when class X extend class Y , then Y is called super class or base class and X is called subclass or derived class.
#------------------
class UavType:
  """
  This is a parent class that is intended to be inherited by other classes
  """
  def calculate_position(self):
    """
    This method is intended to be overridden in subclasses.
    If a subclass doesn't implement it but it is called, NotImplemented will be raised.
    """
    raise NotImplementedError("Base class is not implemented")
class Akinci(UavType):
  """
  This is a subclass of the Shape class, and represents a square
  """
  side_length = 2 # in this example, the sides are 2 units long
  
  def calculate_position(self):
    """
    This method overrides Shape.calculate_area(). When an object of type
    Square has its calculate_area() method called, this is the method that
    will be called, rather than the parent class' version.
    It performs the calculation necessary for this shape, a square, and
    returns the result.
    """
    return self.side_length * 2
class Tb2(UavType):
  """
  This is also a subclass of the Shape class, and it represents a triangle
  """
  base_length = 4
  height = 3
  
  def calculate_position(self):
    """
    This method also overrides Shape.calculate_area() and performs the area
    calculation for a triangle, returning the result.
    """
    return 0.5 * self.base_length * self.height
def get_position(input_obj):
  """
  This function accepts an input object, and will call that object's
  calculate_area() method. Note that the object type is not specified. It
  could be a Square, Triangle, or Shape object.
  """
  print(input_obj.calculate_position())

  
  
def main():
  
  #Polymorphism
  baykar = UAV()
  kaplan = UGV()
  robots(baykar)
  robots(kaplan)
  #------------
  
  #BASIC POLYMORPHISM
  #uav_obj = UavType()
  akinci_obj = Akinci()
  tb2_obj = Tb2()
  
  #get_position(uav_obj)
  get_position(akinci_obj)
  get_position(tb2_obj)
  #-------------------


if __name__ == '__main__':
    main()