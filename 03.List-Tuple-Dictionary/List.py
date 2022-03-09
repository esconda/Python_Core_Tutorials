import os
#Author: Burak Dogancay
def main():

    #List can store thousands of variables
    mylist = [1,2,3,4,5,6,7]
    longerlist = [[1,2,3,4,5],[3,4,5,6,7]]
    anothertypelist = [["object"],[1,2,3,4]]
    mylist_str = ["pazartesi","salı","çarşamba"]
    removed_last_list = []

    #get specific value from list #IMPORTANT
    getlist = [oldval for oldval in mylist if oldval%2==0]
    print("Even number identition : ",getlist)

    #Concanating two list
    conclist1 = [1,2,3,4,5]
    conclist2 = [6,7,8,9]
    concend = conclist1+conclist2
    print("Concanated list = ", concend)

    #another way of creating 2D list
    col=5
    row=7
    twodlist = [[0]*col]*row
    print("2D List ",twodlist)
    print(anothertypelist)

    #List shape

    #Mylist operations 
    mylist.append(8)#add 8 to end of the list
    mylist.insert(1,12)# insert 12 to list
    mylist.pop(6)#remove 6 from the list
    mylist.remove(2)#remove 2 from the list
    #mylist.clear()#clear the list
    mylist.reverse()#reverse list

    #Sorting List
    sortinglist = mylist
    sortinglist.sort()

    #empty list and append
    emptylist = list()
    emptylist.append(mylist)

    index = mylist_str.index("çarşamba")


    print("removed list",mylist)
    print("Index of the list : ", index)
    print("Longer list: ", longerlist[1][-1])
    print("List-Tuple-Dictionary variables length :" , len(mylist))
    print("Write string based list :", mylist_str[2])
    print("Type of the list : ", type(mylist_str))
    print("Get last element of the list : ",mylist[-1]) #get last element of the list
    print("Divide the list : " , mylist[0:4]) #get first 4 element in list
    print("Get first element ",longerlist[0:1])
    print("Appending ,removing,reversing list : ", mylist)
    print("Sorting List-Tuple-Dictionary :", sortinglist)
    print("index : ",mylist.index(4,0,mylist[-1]))
    print("return the number of times x appears in the list : ",concend.count(2))
    print("reverse the element of the list :", )

    #LIST COMPREHENSIONS
    #List comprehensions in Python are concise, syntactic constructs. They can be utilized to generate lists from other
    #lists by applying functions to each element in the list
    #[ <expression> for <element> in <iterable> ]
    #[ <expression> for <element> in <iterable> if <condition> ]

    squares = [x * x for x in (1, 2, 3, 4)]
    # squares: [1, 4, 9, 16]

    # Get a list of uppercase characters from a string
    [s.upper() for s in "Hello World"]
    # ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

    # Strip off any commas from the end of strings in a list
    [w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
    # ['these', 'words', 'mostly', 'have,commas']

    # Organize letters in words more reasonably - in an alphabetical order
    sentence = "Beautiful is better than ugly"
    ["".join(sorted(word, key=lambda x: x.lower())) for word in sentence.split()]
    # ['aBefiltuu', 'is', 'beertt', 'ahnt', 'gluy']

    # When using if/else together use them before the loop
    [x if x in 'aeiou' else '*' for x in 'apple']
    # ['a', '*', '*', '*', 'e'

    #Double Iteration
    #[str(x)
    #   for i in range(3)
            #for x in foo(i)
    #]
    a = [str(x) for i in range(3) for x in [1,2,3,4,5]]
    print(a)
    #--------------------------------------------------------

    #CONDITIONAL LIST COMPREHENSION

    [x for x in range(10) if x % 2 == 0]
    # Out: [0, 2, 4, 6, 8]

    [x if x % 2 == 0 else None for x in range(10)]
    # Out: [0, None, 2, None, 4, None, 6, None, 8, None]

    [2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]
    # Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

    [x if x > 2 else '*' for x in range(10) if x % 2 == 0]
    # Out: ['*', '*', 4, 6, 8]

    [x if (x > 2 and x % 2 == 0) else '*' for x in range(10)]
    # Out:['*', '*', '*', '*', 4, '*', 6, '*', 8, '*']
    #---------------------------------------------------

    #Changing Types in a List
    # Convert a list of strings to integers.
    items = ["1", "2", "3", "4"]
    [int(item) for item in items]
    # Out: [1, 2, 3, 4]

    # Convert a list of strings to float.
    items = ["1", "2", "3", "4"]
    map(float, items)
    # Out:[1.0, 2.0, 3.0, 4.0]
    #---------------------------------------------------
if __name__=='__main__':
    main()