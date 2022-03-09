import os
#Author: Burak Dogancay
def main():

    #float
    double = 10.4

    #int
    int =20

    #string
    string = "my string"
    string_length = len(string)


    print("double variable :" , type(double), type(int), type(string),string_length,string[4])


if __name__=='__main__':
    main()