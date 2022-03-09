import os
#Author: Burak Dogancay
def main():

    i=0
    mylist = [1,2,3,4,5,6]

    while(i<4):
        print(i)
        i+=1

    each = 0
    restrict = len(mylist)
    count1=0
    while(each < restrict ):
        count1 = count1 + mylist[each] #summing each value
        each = each +1
        print(count1)

    #QUİZ,Listenin içindeki en küçük sayıyı bul
    quizlist = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]
    quizlist.sort()
    print("lower value", quizlist[0])
    print("lower value with min function", min(quizlist))

    # another method
    minimum = 10000
    lowest_value = 0
    for each in quizlist:
        if(each<minimum):
            minimum = each
        else:
            continue
    print("for loop methode sorting lowest value :",minimum)

if __name__=='__main__':
    main()