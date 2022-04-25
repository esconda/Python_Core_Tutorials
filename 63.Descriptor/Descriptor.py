# Author: Burak Dogancay
#MAKE IT MORE CLEAR
#There are two different types of descriptors. Data descriptors are defined as objects that define both a __get__()
#and a __set__() method, whereas non-data descriptors only define a __get__() method. This distinction is
#important when considering overrides and the namespace of an instance's dictionary. 

#To make a read-only data descriptor, define both get() and set() with the set() raising an AttributeError when called.
#Defining the set() method with an exception raising placeholder is enough to make it a data descriptor
 
#descr.__get__(self, obj, type=None) --> value
#descr.__set__(self, obj, value) --> None
#descr.__delete__(self, obj) --> None
#-------------------------------SIMPLE DESCRIPTOR CLASS-----------------------------------------
class DescrClass(object) : 
    uavVar ='tb2'
    
    def __get__(self, obj , objtype = None):
        print("Getting global class variable",self.uavVar)
        return self.uavVar
    
    def __set__(self,obj,val):
        print("Setting global class variable",val)
        self.uavVar = val
    
    def __delete__(self,obj):
        print("Deleting...")
        del self.uavVar

class refClass():
    desc = DescrClass()
        
def main():
    #SIMPLE DESCRIPTOR EXAMPLE
    ref = refClass()
    ref.desc #Getting global var
    ref.desc = 'Akinci' # Setting
    ref.desc #Getting variable after change
    del ref.desc #Deleting
    ref.desc #Getting again
    #--------------------------
    

if __name__ == '__main__':
    main()