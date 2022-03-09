import numpy as np
#Author: Burak Dogancay
def main():
    x = np.zeros((5,4))#fill x with zeros
    y = np.ones ((5,4),np.int32)#fill numpy with ones
    false_positives = np.zeros((0,))
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    z = np.array([[2,3,4],[5,6,7]])#create array with variables
    a = x[:,2]#get all values of x position of 3 which means 2
    a1= x.strides# shows number of bytes for each column here we have 4 element with 8 bytes value and it shows (8*4 total number of bytes ,8 bytes)
    shapex,shapey = x.shape# it show how many column and row is available innumpy array x = (5,4)

    #Box example for Machine learning
    ybatch=np.zeros((16,13,13,5,6))

    box = [1, 2, 3, 20]
    ybatch[15,12,12,4,0:4]=box
    ybatch[15,12,12,4,4] = 1.
    ybatch[15,12,12,4,5]=1

    maxvalueybatch = np.max(ybatch)
    minvalueybatch = np.min(ybatch)


    ybatch[..., 5:] = ybatch[..., 4][..., np.newaxis]
    # print(ybatch)
    # print(ybatch[..., 5])
    # print(ybatch.shape[:3])
    #---------------------------------

    x[...] = 10 #fill all values in x with 10
    x[3][2]=9 ## fill specified position with 9

    # for i in range(0,20):
    #     false_positives = np.append(false_positives,1)
    #
    # false_positives = np.cumsum(false_positives)

    #DELETE SPECIFIED AXIS VALUE
    arr = np.delete(arr, 1, 0)#remove xaxis 0 and yaxis 1 which is [5, 6, 7, 8]

    # x[2,0:4] = box
    print("array", arr)
    print("array shape",arr.shape)

    print("x array : ",x)
    print("y array : ",y)
    print("z array : ",z)
    print("array size of the z :",z.size)
    print("a array : ",a)
    print ("a1 strides",a1)
    print("row :",shapex," column :", shapey," of x")
    print("false positives: ", false_positives)
    print("sinirla", x[3,0:4]) #3.sıraların hepsi
    print("Box : ", box)
    print("Maximum value of ybatch", maxvalueybatch)
    print("Minimum value of ybatch", minvalueybatch)
    #print("ybatch: " , ybatch )

if __name__ == '__main__' :
    main()