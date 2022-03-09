import os
#Author: Burak Dogancay
class Myfirstclass(object):

    zamorani = 1.8
    counter= 0

    def __init__(self,isim,soyisim,maas):#Constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim+"@gmail.com"

        self.counter = self.counter+1

    def giveNameSurname(self):
        return self.isim +" "+self.soyisim

    def zam_yap(self):#For updating variable
        self.maas =  self.maas + self.maas * self.zamorani
        return self.maas

def main():
    #These two constructor is different
    classconstructor = Myfirstclass("ali", "veli",100)#create constructor
    print("Zamli maasi", classconstructor.zam_yap())#reach everything inside of class
    print("Constructor 1 :",classconstructor.counter)

    classconstructor1 = Myfirstclass("Burak","Dogancay",200)
    print("Constructor 2 :",classconstructor1.counter)


#-------------CLASS EXAMPLE RUN CLASS IN ARRAY LIST----------------
    calisan1 = Myfirstclass("ali","osman",200)
    calisan2 = Myfirstclass("burak","dogancay",300)
    calisan3 = Myfirstclass("erdem", "yenice",400)

    mylist = [calisan1,calisan2,calisan3]

    maximum_maas = -1
    index = -1

    for each in mylist:
        if(each.maas>maximum_maas):
            maximum_maas = each.maas
            index = each

    print("maximum maas", maximum_maas)
    print("index :", index.giveNameSurname())
#-------------------------------------------------------------------

if __name__=='__main__':
    main()