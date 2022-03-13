import os
import operator
from cv2 import DIST_FAIR
# Author: Burak Dogancay


def main():
  # A tuple is an immutable list of values. Tuples are one of Python's simplest and most common collection types, and
  # can be created with the comma operator

    mylist = (1, 2, 3, 3, 4, 5, 6)
    mylist_str = ("monday", "tuesday", "wednesday")

    print("List-Tuple-Dictionary variables length :",
          len(mylist))  # size of the mylist
    print("Write string based tuple :", mylist_str[2])
    print("Type of the tuple : ", type(mylist_str))
    # get last element of the list
    print("Get last element of the tuple : ", mylist[-1])
    print("Divide the tuple : ", mylist[0:4])  # get first 4 element in list
    print("Appending ,removing,reversing tuple : ", mylist)
    print("how many number of 3 is available in tuple :", mylist.count(3))
    print("index of the tuple :", mylist.index(3, 0, mylist[-1]))  # get index of the three
    print("---------------------")
    

    # COMPREHENSION WITH TUPLES
    [x + y for x, y in [(1, 2), (3, 4), (5, 6)]]
    # Out: [3, 7, 11]

    [x + y for x, y in zip([1, 3, 5], [2, 4, 6])]
    # Out: [3, 7, 11]

    # Tuples are Immutable.One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot
    # add or modify items once the tuple is initialized.
    # For Example
    #uav = ("tb2", "tb3", "akinci")
    #uav[0] = "preadtor"  # Gives error

    # ----PACKING AND UNPACKING TUPLES----
    # Note that a one-value tuple is also a tuple. To tell Python that a variable is a tuple and not a single value you can use
    x = 10  # a is the value 10
    x = 10,  # a is the tuple (10,)
    x = (10,)  # a is the tuple (1,)
    x = (10)  # a is the value 10 and not a tuple

    # unpacking AKA multiple assignment
    x, y, z = (1, 2, 3)
    # x == 1
    # y == 2
    # z == 3
    
    # --------------------------------------------------------
    
    # ----BUILT IN TUPLE FUNCTIONS----
    tuple1 = ('z', 'y', 'a', 'b', 'd')
    tuple2 = ('4','5','8')
    tuple3 = ('z', 'y', 'a', 'b', 'd')

    #Compare Tuples
    print("Tuple1 vs Tuple2 : " ,operator.eq(tuple1,tuple2))
    print("Tuple2 vs Tuple3 : ", operator.eq(tuple2,tuple3))
    print("Tuple1 vs Tuple3 : ", operator.eq(tuple1,tuple3))
    print("---------------------")
    
    #Max of Tuple
    print("Max Tuple1 : " ,max(tuple1))
    print("Max Tuple2 : ", max(tuple2))
    print("---------------------")
    
    #Min of Tuple
    print("Min Tuple1 : " ,min(tuple1))
    print("Min Tuple2 : ", min(tuple2))
    print("---------------------")
    
    #Convert List Into Tuple
    myList = [1,2,3,4,5]
    myTuple = tuple(myList)
    print("Convertion List to Tuple : ", myTuple)
    print("---------------------")

    # --------------------------------------------------------
    
    # ----INDEXING TUPLES----
    xTuple = (1, 2, 3)
    xTuple[0] # 1
    xTuple[1] # 2
    xTuple[2] # 3
    #xTuple[3] # IndexError: tuple index out of range
    
    xTuple[-1] # 3
    xTuple[-2] # 2
    xTuple[-3] # 1
    #xTuple[-4] # IndexError: tuple index out of range

    #Indexing Range of Elements
    print("Get instead of last elements: ",xTuple[:-1]) # (1, 2)
    print("Get last elements: ",xTuple[-1:]) # (3,)
    print("Get between ",xTuple[1:3]) # (2, 3)
    print("---------------------")
    # --------------------------------------------------------
    
    # ----REVERSING TUPLES----
    normTuple = (1, 2, 3)
    revTuple = normTuple[::-1]
    
    print("Normal Tuple: ", normTuple)
    print("Reverse Tuple: ",revTuple) 
    print("Another Method of Reversing Tuple: ",tuple(reversed(normTuple)))
    print("---------------------")
    # --------------------------------------------------------


if __name__ == '__main__':
    main()
