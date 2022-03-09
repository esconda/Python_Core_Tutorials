import os
#Author: Burak Dogancay
import numpy as np
#INDEXING AND SLICING
def main():

   array  = np.array([1,2,3,4,5,6,7])
   reversearray = array[::-1]
   array2 = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])

   print("definition of array ",array)
   print("Array", array[0])
   print("Index", array[0:4]) #print 0 to 4
   print("Writing array2 :",array2)
   print("array shape :", array.shape)
   print("Reversing array :", reversearray) #reverse of the array
   print("get all values of first column of array2:", array2[:,1])
   print("get elements of array2", array2[:1])
   print("get specified area of array2 :", array2[1,0:4])
   print("get last column values of array2 :", array2[-1,:])
   print ("get last row values of array2 :", array2[:,-1])

if __name__=='__main__':
    main()