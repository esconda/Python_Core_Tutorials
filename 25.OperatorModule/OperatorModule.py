#Author: Burak Dogancay
#Author: Burak Dogancay
from operator import itemgetter
from itertools import groupby
from operator import methodcaller

def itemGetter():
    #Grouping the key-value pairs of a dictionary by the value with itemgetter:
    myDict = {"uav1": 1, "uav2": 1, "uav3":3}
    sortItems = dict((i, dict(v)) for i, v in groupby(myDict.items(), itemgetter(1)))
    groupItems = [i for i, v in groupby(myDict.items(), itemgetter(1))]
    print("ITEMGETTER OPERATIONS")
    print("Sort by velue Anka : ", sortItems,groupItems)
    print("---------------------")
 
  
def methodCaller():
    myList = ["TB2","AKINCI","AKSUNGUR","ANKA"]
    sortList = lambda a : [a for a in myList if a =="ANKA" or a=="TB2"] #LAMBDA FUNCTİON THAT WE MENTİONED BEFORE
    methodeCaller = methodcaller('itemGetter')
    print("METHODCALLER OPERATIONS")
    print("Sort by velue ANKA AND TB2 : ", sortList(1))
    print("---------------------")
    
def main():
    itemGetter()
    methodCaller()
    
if __name__ == '__main__':
    main()
