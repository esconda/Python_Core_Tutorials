from enum import Enum
#Author: Burak Dogancay
def main():
    firstDictionary = {10,20,30,40,50}
    secondDictionary = {60,70,80,30,40}

    #Intersection
    intersection = firstDictionary.intersection(secondDictionary) #Interserction
    intersectionAlternative = firstDictionary & secondDictionary

    #Union
    union = firstDictionary.union(secondDictionary)
    unionAlternative = firstDictionary | secondDictionary

    # Difference
    difference = firstDictionary.difference(secondDictionary)
    difAlternative = firstDictionary- secondDictionary

    # Symmetric difference with
    symetricDif = firstDictionary.symmetric_difference(secondDictionary)
    symDifAlternative = firstDictionary ^ secondDictionary

    # Superset check
    superSet = firstDictionary.issuperset(secondDictionary)
    superSetAlternative = firstDictionary >= secondDictionary

    # Subset check
    subSet = firstDictionary.issubset(secondDictionary)
    subSetAlternative = firstDictionary <= secondDictionary

    # Disjoint check
    disJoint = firstDictionary.isdisjoint(secondDictionary)
    disJointAlternative = firstDictionary.isdisjoint(secondDictionary)

    print("First Dictionary", firstDictionary)
    print("Second Dictionary", secondDictionary)

    print("Intersection : ", intersection)
    print("Intersection Alternative : " ,intersectionAlternative)

    print("Union : ", union)
    print ("Union Alternative : ", unionAlternative)

    print("Difference : ",difference)
    print("Difference Alternative : ", difAlternative)

    print("Symetric Difference : ", symetricDif)
    print("Symetric Difference Alternative : ", symDifAlternative)

    print("SuperSet : ", superSet)
    print("SuperSet Alternative : ", superSetAlternative)

    print("SubSet : ", subSet)
    print("SubSet Alternative : ", subSetAlternative)

    print("Disjoint : ", disJoint)
    print("Disjoint Alternative : ", disJointAlternative)

    # Add and Remove
    s = {1, 2, 3}
    s.add(4)  # s == {1,2,3,4}
    s.discard(3)  # s == {1,2,4}
    s.discard(5)  # s == {1,2,4}
    s.remove(2)  # s == {1,4}
    #s.remove(2)  # KeyError!

    #Get the unique elements of a list
    restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
    unique_restaurants = set(restaurants)
    print("List : ", restaurants)
    print("List to Dictionary : ",unique_restaurants)

    #SET COMPREHENSIONS
    {x for x in range(5)}
    # Out: {0, 1, 2, 3, 4}

    # A set of even numbers between 1 and 10:
    {x for x in range(1, 11) if x % 2 == 0}
    # Out: {2, 4, 6, 8, 10}
    #------------------------------------------------
if __name__=='__main__':
    main()