import os
#Author: Burak Dogancay
class Myfirstclass(object):
    def __init__(self,name,surname,salary):#Constructor
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname+"@gmail.com"

    def giveNameSurname(self):
        return self.name +""+self.surname


def main():
    classconstructor = Myfirstclass("ali", "veli",100)
    print("variable",classconstructor.name)
    print("Give Full Name Function : ", classconstructor.giveNameSurname())


if __name__=='__main__':
    main()