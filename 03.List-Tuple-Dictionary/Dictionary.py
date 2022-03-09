import os
#Author: Burak Dogancay
from collections import OrderedDict
def trying(dictionary):
    return dictionary

def main():
    # return more than one value with names with dictionary and create your own database
    mydictionary = {"ali": 32, "veli": 45,"ayse":13}# ali,veli,ayşe = keys
    emptyDict = dict()

    # mylist.append(8)#add 8 to end of the list
    # mylist.remove(2)#remove 2 from the list
    # mylist.reverse()#reverse list
    #
    # sortinglist = mylist
    # sortinglist.sort()


    print("Dictionary variables length :" , len(mydictionary))
    print("Dictionary Keys : ",mydictionary.keys())
    print ("Values of the Dictionary: ", mydictionary.values())
    print("Key and Values are : ", mydictionary.items())
    print("Type of the dictionary : ", type(mydictionary))
    print("Dictionary : ", mydictionary)
    print("Get specified dictionary value",mydictionary["ali"])
    print("Type of specified variable key", type(mydictionary["ali"]))
    print("Return dictionary from function", trying(mydictionary))
    print("Empty Dict : ",dict)

    #MERGING DICTIONARIES
    fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
    dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
    fishdog = {**fish, **dog}

    for value in fishdog:
        print("Key of the dictionary : ",value)
    for value in fishdog.values():
        print("Value of the dictionary :",value)
    #--------------------------------------------

    #CREATING ORDER IN DICTIONARY
    d = OrderedDict()
    d['first'] = 1
    d['second'] = 2
    d['third'] = 3
    d['last'] = 4
    # Outputs "first 1", "second 2", "third 3", "last 4"
    for key in d:
        print(key, d[key])
    #--------------------------------------------

    #Unpacking dictionaries using the ** operator
    # dictionary = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    # print("Unpacked of the dict : ",**dictionary.keys())
    #--------------------------------------------

    #The dict() constructor
    dict(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
    dict([('d', 4), ('e', 5), ('f', 6)])  # {'d': 4, 'e': 5, 'f': 6}
    dict([('a', 1)], b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
    dict({'a': 1, 'b': 2}, c=3)  # {'a': 1, 'b': 2, 'c': 3}
    #--------------------------------------------

    #DICTIONARY COMPREHENSION
    {x: x * x for x in (1, 2, 3, 4)}
    # Out: {1: 1, 2: 4, 3: 9, 4: 16}

    dict((x, x * x) for x in (1, 2, 3, 4))
    # Out: {1: 1, 2: 4, 3: 9, 4: 16}

    {name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6}
    # Out: {'Exchange': 8, 'Overflow': 8}

    #Starting with a dictionary and using dictionary comprehension as a key-value pair filter
    initial_dict = {'x': 1, 'y': 2}
    {key: value for key, value in initial_dict.items() if key == 'x'}
    # Out: {'x': 1}

    #Swapping Operations
    # The zip() function returns a zip object, which is an iterator
    # of tuples where the first item in each passed iterator is paired together,
    # and then the second item in each passed iterator are paired together etc.
    my_dict = {1: 'a', 2: 'b', 3: 'c'}
    swapped = {v: k for k, v in my_dict.items()}
    #swapped = dict((v, k) for k, v in my_dict.iteritems())
    swappedOne = dict(zip(my_dict.values(), my_dict)) #The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
    swappedTwo = dict(zip(my_dict.values(), my_dict.keys()))
    swappedThree = dict(map(reversed, my_dict.items()))

    print("Swapped Operation",swapped)
    print("Swapped Operation with zip", swappedOne)
    print("Swapped Operation", swappedTwo)
    print("Swapped Operation", swappedThree)
    # Out: {a: 1, b: 2, c: 3}

    #Merging Dictionaries
    dict1 = {'w': 1, 'x': 1}
    dict2 = {'x': 2, 'y': 2, 'z': 2}
    {k: v for d in [dict1, dict2] for k, v in d.items()}
    # Out: {'w': 1, 'x': 2, 'y': 2, 'z': 2}
    print([dict1,dict2])
    #--------------------------------------------
if __name__=='__main__':
    main()