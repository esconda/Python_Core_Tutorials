# Author: Burak Dogancay
import pickle
import os
#The pickle module implements an algorithm for turning an arbitrary Python object into a series of bytes. This
#process is also called serializing the object. The byte stream representing the object can then be transmitted or
#stored, and later reconstructed to create a new object with the same characteristics
def getSpecFile(pFileName):
  location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
  fileName= os.path.join(location,pFileName)#add file name to folder location
  return fileName

def serializingData():
  # An arbitrary collection of objects supported by pickle.
  dictData = {
          'a': [1, 2.0, 3, 4+6j],
          'b': ("character string", b"byte string"),
          'c': {None, True, False}
          }
  with open(getSpecFile("myData.pickle"),"wb") as file:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(dictData, file, pickle.HIGHEST_PROTOCOL)
  
def deserializingData():
  with open(getSpecFile('myData.pickle'), 'rb') as file:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    myData = pickle.load(file)
  print("Deserialized data is : ",myData)
  
  #Customized pickle data
  #What will be pickled can be defined in __getstate__ method. This method must return something that is picklable
class UAV(object):
  def __init__(self, important_data):
    self.important_data = important_data
    # Add data which cannot be pickled:
    self.func = lambda: 7
    # Add data which should never be pickled, because it expires quickly:
    self.is_up_to_date = False
  def __getstate__(self):
    return [self.important_data] # only this is needed
  
  def __setstate__(self, state):
    self.important_data = state[0]
    self.func = lambda: 7 # just some hard-coded unpicklable function
    self.is_up_to_date = False # even if it was before pickling
def main():
  serializingData()
  deserializingData()
  
  #Costumized pickle
  a1 = UAV('UAV İS AVAİLABLE')
  serialize = pickle.dumps(a1)
  a2 = pickle.loads(serialize)
  print(a2.important_data)

if __name__ == '__main__':
    main()