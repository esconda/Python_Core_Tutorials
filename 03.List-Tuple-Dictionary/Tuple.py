import os
#Author: Burak Dogancay
def main():

    mylist = (1,2,3,3,4,5,6)
    mylist_str = ("pazartesi","salı","çarşamba")



    print("List-Tuple-Dictionary variables length :" , len(mylist))
    print("Write string based tuple :", mylist_str[2])
    print("Type of the tuple : ", type(mylist_str))
    print("Get last element of the tuple : ",mylist[-1]) #get last element of the list
    print("Divide the tuple : " , mylist[0:4]) #get first 4 element in list
    print("Appending ,removing,reversing tuple : ", mylist)
    print("how many number of 3 is available in tuple :" , mylist.count(3))
    print("index of the tuple :", mylist.index(3,0,mylist[-1])) # get index of the three

    #COMPREHENSION WITH TUPLES
    [x + y for x, y in [(1, 2), (3, 4), (5, 6)]]
    # Out: [3, 7, 11]

    [x + y for x, y in zip([1, 3, 5], [2, 4, 6])]
    # Out: [3, 7, 11]


if __name__=='__main__':
    main()