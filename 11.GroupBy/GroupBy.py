import itertools
#Author: Burak Dogancay
def main():
    # #In Python, the itertools.groupby() method allows developers to group values of an iterable class based on a
    # specified property into another iterable set of values.

    #Example 1
    things = [("animal", "Lion"), ("animal", "Duck"), ("plant", "Cactus"), ("Vehicle", "Porsche"), \
          ("vehicle", "speed boat"), ("vehicle", "school bus")]
    ddictionary = {}
    f = lambda x: x[0]
    for key, group in itertools.groupby(sorted(things, key=f), f):
        ddictionary[key] = list(group)
    
    print("*********************************")
    print(ddictionary)
    print("*********************************")
    #------------

    #Example 2
    c = itertools.groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
    dictionary = {}
    for k, v in c:
        dictionary[k] = list(v)

    print(dictionary)
    print("*********************************")
    #------------

    #Example 3
    list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), \
                   'wombat', 'mongoose', 'malloo', 'camel']
    c = itertools.groupby(list_things, key=lambda x: x[0])
    dictionary = {}
    for k, v in c:
        dictionary[k] = list(v)
        
    print(dictionary)
    print("*********************************")
    #------------

if __name__=='__main__':
    main()