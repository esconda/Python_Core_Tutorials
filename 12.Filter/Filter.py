import itertools
#Author: Burak Dogancay
def long_name(name):
    return len(name) > 5

def main():
    names = ['Fred', 'Wilma', 'Barney']
    itertools.filterfalse(long_name, names)  # as generator (similar to python 3.x filter builtin)
    # Out: <itertools.ifilter at 0x4197e10>
    list(itertools.filterfalse(long_name, names))  # equivalent to filter with lists
    # Out: ['Barney']
    
if __name__=='__main__':
    main()