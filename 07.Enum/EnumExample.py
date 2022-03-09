from enum import Enum
#Author: Burak Dogancay
def main():
    #Enum Creation Example
    class Color(Enum):
        red = 1
        green = 2
        blue = 3

    print(Color.red.value) #get spesified enum value
    print(Color.green.name) #get spesified enum name
    print(Color(3).name) #get 3. enum
    print(Color['red'].name) #access enum member name by attr name
    print(Color['green'].value) #access enum member value by attr name

    #ENUM ITERATION
    enumInfo = [c for c in Color] #Iterating enum by loop
    print(enumInfo)
    print ("Enum Info First member Value is :" +str(enumInfo[1].name))
    print ("Enum Info Third member Value is : " + str(enumInfo[2].value))

if __name__=='__main__':
    main()