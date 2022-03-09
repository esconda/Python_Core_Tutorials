import os
#Author: Burak Dogancay
class Myfirstclass(object):
    def __init__(self,isim,soyisim,maas):#Constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim+"@gmail.com"

    def giveNameSurname(self):
        return self.isim +""+self.soyisim


def main():
    classconstructor = Myfirstclass("ali", "veli",100)
    print("variable",classconstructor.isim)
    print("Givesurname function : ", classconstructor.giveNameSurname())


if __name__=='__main__':
    main()