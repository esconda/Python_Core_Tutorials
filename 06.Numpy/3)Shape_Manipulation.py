import os
#Author: Burak Dogancay
import numpy as np

def main():
    array = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])

    print("array", array)

    #flattening vector of the array
    vectorofarray = array.ravel()# it makes multidimensional array as 1d vector
    print("1D vector of the array : ",vectorofarray)

    #converts 1D vector to multidimensional array
    vectortoarray = vectorofarray.reshape(3,6)
    print("1d vector to [3,3] array : ", vectortoarray)

    #transpose  = yatay şekildeki elementleri dik olarak yazmak
    transpose = vectortoarray.transpose()
    print("Transpose of the array : ", transpose)
    print("Transposed array shape: ", transpose.shape)
    print("Reshape of the matrix : " ,transpose.reshape(9,2))


if __name__=='__main__':
    main()