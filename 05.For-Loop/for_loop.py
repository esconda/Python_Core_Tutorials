import os
#Author: Burak Dogancay
def main():

    #List comprehension it returns even numbers as a list
    list = [1,2,3,4,5,6,7]
    splitspecial = [i for i in list if i%2==0]
    print("Splitted values : " , splitspecial)


    for each in range(1,11):
        print("each value : ",each)

    for each in "ankara ist":
        print("each value :",each)

    for each in "ankara ist".split():
        print("each value :",each)

    #If you want to loop though both the elements of a list and have an index for the elements as well, you can use
    #Python's enumerate function:
    for index, item in enumerate(['one', 'two', 'three', 'four']):
        print(index, '::', item)


    #sum of the values in 2 different way
    #without for loop
    mylist = [1,2,3,4,5,6,7,8]
    print("sum of the values",sum(mylist))

    #with for loop
    count =0
    for each in mylist:
        count = count + each

    print("summing all values with for loop",count)
    #------------------------------------

    #BREAK AND CONTINUE IN LOOPS
    #Example break 1
    i = 0
    while i < 7:
        print(i)
        if i == 4:
            print("Breaking from loop")
            break
        i += 1
    #Example break 2
    while True:
        for i in range(1, 5):
            if i == 2:
                print("Breaking from the loop")
                break  # Will only break out of the inner loop!
        break

    #Example continue 1
    for i in (0, 1, 2, 3, 4, 5):
        if i == 2 or i == 4:
            continue
        if i == 5:
            break
        print(i)
    #Use return from within a function as a break
    #------------------------------------------

    #PASS STATEMENT
    for x in range(10):
        pass#we don't want to do anything, or are not ready to do anything here, so we'll pass
    #----------------------------------------------------------------------------------------

    #ITERATING OVER DICTIONARIES
    d = {"a": 1, "b": 2, "c": 3}
    for key in d:
        print(key)#prints a,b,c

    for value in d.values():
        print(value) # print 1,2,3
    #------------------------------------


if __name__=='__main__':
    main()