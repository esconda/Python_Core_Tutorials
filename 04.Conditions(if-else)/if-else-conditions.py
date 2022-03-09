import os
#Author: Burak Dogancay
def yeartocentury(year):
    str_year = str(year)

    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"): #100,200,300,400
            return int(str_year[0])
        else :
            return int(str_year[0])+1
    else:#1750,1700,1805
        if(str_year[2:4]=="00"):#1700,1900,1100
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1

def main():

    var1 = 10
    var2 = 10

    if (var2>var1):
        print("var2 is bigger than var1")

    elif(var2==var1):
        print("var2 is equal to var1")

    else:
        print("var2 is lower than var1")


    #with List example
    mylist = [1,2,3,4,5,6]
    value = 8
    mydictionary = {"ali": 32, "veli": 45, "ayse": 13}

    if value in mylist:
        print("Value is available in list")
    else :
        print("value is not available in list")
    #---------------------------------------------

    #Dictionary examples
    keys = mydictionary.keys()

    if "ali" in keys:
        print("evet")
    else :
        print("hayır")
    #---------------------------------------------

    #example with function
    print("Century according to year :",yeartocentury(1990))

    #SOME OTHER EXAMPLES
    n=5
    "Greate than 2" if n>2 else "Smaller than 2"
    # Out: 'Greater than 2'
    n = 5
    print("Hello") if n > 10 else print("Goodbye") if n > 5 else print("Good day") # it can be use for lambda functions

    #BOOLEAN LOGIC EXPRESSIONS
    a=1
    b=6
    if a > 2 and b > 2:
        print('yes')
    else:
        print('no')
    #Another Example
    if a in (3, 4, 6):
        print('yes')
    else:
        print('no')

    #IS VS ==
    a = 'Python is fun!'
    b = 'Python is fun!'
    a == b  # returns True
    a is b  # returns False
    a = [1, 2, 3, 4, 5]
    b = a  # b references a
    a == b  # True
    a is b  # True
    b = a[:]  # b now references a copy of a
    a == b  # True
    a is b  # False [!!]

if __name__=='__main__':
    main()