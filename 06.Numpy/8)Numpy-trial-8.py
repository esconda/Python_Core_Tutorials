import numpy as np
#Author: Burak Dogancay
def main():
    name = np.array([["Burak","Another"],["Ahmet","Mehmet"]])
    word = name[:,1]


    print("Show Array : ",name)
    print("Vertical show : ", name.transpose())
    print("Writing word : ", word)

if __name__=='__main__':
    main()