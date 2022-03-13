import os
#Author: Burak Dogancay
class Myfirstclass(object):

    zamorani = 1.8
    counter= 0

    def __init__(self,name,surname,salary):#Constructor
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname+"@gmail.com"

        self.counter = self.counter+1

    def giveNameSurname(self):
        return self.name +" "+self.surname

    def zam_yap(self):#For updating variable
        self.salary =  self.salary + self.salary * self.zamorani
        return self.salary

def main():
    #These two constructor is different
    classconstructor = Myfirstclass("ali", "veli",100)#create constructor
    print("Increased Salary", classconstructor.zam_yap())#reach everything inside of class
    print("Constructor 1 :",classconstructor.counter)

    classconstructor1 = Myfirstclass("Burak","Dogancay",200)
    print("Constructor 2 :",classconstructor1.counter)


#-------------CLASS EXAMPLE RUN CLASS IN ARRAY LIST----------------
    calisan1 = Myfirstclass("ali","osman",200)
    calisan2 = Myfirstclass("Burak","Dogancay",300)
    calisan3 = Myfirstclass("Yunus Emre", "",400)

    mylist = [calisan1,calisan2,calisan3]

    maximum_salary = -1
    index = -1

    for each in mylist:
        if(each.salary>maximum_salary):
            maximum_salary = each.salary
            index = each

    print("Maximum Salary", maximum_salary)
    print("Index :", index.giveNameSurname())
#-------------------------------------------------------------------

if __name__=='__main__':
    main()