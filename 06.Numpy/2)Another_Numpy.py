import numpy as np
#Author: Burak Dogancay

def main():
    array = np.array([1,2,3,4,5,6])
    array1 = array.reshape(2,3)

    print("array shape",array1.shape)
    print("first shape",array1.shape[0])
    print("dimension of the array :",array.ndim)
    print("dimension of the array1 :", array1.ndim)
    print("data type of the arrey : ", array.dtype.name)
    print("Size of the array1 :", array1.size)

    arraymultisize = np.array([[1,2,3,4,5], [6,7,8,9,10], [9,10,11,12,13]])
    print(arraymultisize.shape)


    zerosarray = np.zeros((3,4))#allocation list.append memoryi yorarbu nedenle numpy array ile alocate ederiz, sonra içine yerleştiririz
    print("zeros array shape: ", zerosarray.shape)
    print("empty zeros", zerosarray.dtype.name)

    a = np.arange(10,50,5) #write 20 numbers between 10 and 50
    print("increase 5 between 10 and 50", a)
    print("shape of a", a.shape)

    a1 = np.linspace(10,50,20) #write 20 numbers between 10 and 50
    print("write 20 numbers between 10 and 50 ",a1)

    firstnumpy = np.array([1,2,3,4,5])
    secondnumpy = np.array([6,7,8,9,10])

    print("Summing :", firstnumpy + secondnumpy)
    print("Minus :", secondnumpy - firstnumpy)
    print("Square : ", firstnumpy**2)
    print("Division", secondnumpy/firstnumpy)
    print("Sinus Value", np.sin(firstnumpy))


    a2 = np.random.random((5,5)) #produces random number
    print("produce random number : ", a2)
    print("sum all numbers in numpy array : ", a2.sum())
    print("Maximum number of the array : ", a2.max() )
    print("Minimum number of the array :", a2.min())

    print("Summation of all columns :", a2.sum(axis=0))
    print("Summation of the rows :", a2.sum(axis=1))
    print("Add numpy array with same numpy array : ", np.add(a2,a2))


if __name__=='__main__':
    main()