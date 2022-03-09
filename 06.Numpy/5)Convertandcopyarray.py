import os
#Author: Burak Dogancay
import numpy as np

def main():

    array = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
    array1 = np.array([[1,3,4,5,6,9],[1,2,3,4,5,7],[6,7,8,9,2,4]])

    #add list to numpy array
    List = [1,2,3,54,67,54]
    mynumpyarray = np.zeros((2,6))
    mynumpyarray[1,...] = List #change all values of index 1 with list
    mynumpyarray[1,:] = List # same as above

    print("numpy array :", mynumpyarray)

    #List to numpy array
    List = [1,2,3,4,5,6]
    numpyarray = np.array(List)
    print("Convert list to numpy array : ", type(numpyarray))

    #Numpy array to List
    List2 = list(numpyarray)
    print("Numpy array to list :", type(List2))

    #Copy one array to other

    copiedarray = array.copy()
    copiedarray[0,2]=5
    print("Before copy : ", array)#array is not changed
    print("After copy : ", copiedarray)#array is changed



if __name__=='__main__':
    main()