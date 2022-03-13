import heapq
import os
import heapq

# Author: Burak Dogancay


def main():
  # To find the largest items in a collection, heapq module has a function called nlargest, we pass it two arguments, the
  # first one is the number of items that we want to retrieve, the second one is the collection name:

    myList_num = [1, 2, 3, 4, 5, 6, 7]
    myList_str = ["togg", "toyota", "volkswagen"]


    # Heap Operations
    print("Largest 3 Value of myList_num : ", heapq.nlargest(3, myList_num))
    print("Smallest 3 Value of myList_num : ", heapq.nsmallest(3, myList_num))
    print("---------------------")
    # --------------------------


    # ----COMPLEX DATA TYPES----
    people = [
        {'firstname': 'Yunus Emre', 'lastname': 'Tusun', 'age': 28},
        {'firstname': 'Burak', 'lastname': 'Dogancay', 'age': 32},
        {'firstname': 'Koray', 'lastname': 'Sarioglu', 'age': 31},
        {'firstname': 'Melih', 'lastname': 'Mete', 'age': 25},
    ]
    
    #Oldest Person
    oldest_person = heapq.nlargest(2, people, key=lambda s: s['age'])
    print("Get 2 oldest person from people : ", oldest_person)
    print("---------------------")
    
    #Youngest Person
    youngest_person = heapq.nsmallest(2, people, key=lambda s: s['age'])
    print("Get 2 youngest person from people : ", youngest_person)
    print("---------------------")
    
    # --------------------------------------------------------


if __name__ == '__main__':
    main()
