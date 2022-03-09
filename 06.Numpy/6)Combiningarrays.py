import os
#Author: Burak Dogancay
import numpy as np

def main():
    array = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
    array1 = np.array([[1,3,4,5,6,9],[1,2,3,4,5,7],[6,7,8,9,2,4]])

    #stacking and combining two arrays
    combinedarray = np.column_stack((array,array1)) # axis and dimensions should be same

    print("Combined Array : ", combinedarray)

    #stacking arrays vertical
    stackingarrayvert = np.vstack((array,array1))# vertical stacking add second array to the end in vertical direction
    print("Stacking array vertical :", stackingarrayvert)

    #stacking arrays horizontal
    stackinghorarray = np.hstack((array,array1))#add arrays horizontally
    print("Stacking array horizontal", stackinghorarray)


if __name__=='__main__':
    main()