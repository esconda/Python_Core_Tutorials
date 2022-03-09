#Author: Burak Dogancay
class mysuperclass(object):
    def print(self):
        print('Super class')
#Overriding with superclass
class Overriding(mysuperclass):
    def print(self):
        print('Overriding')

class subclass(mysuperclass):
    def anotherprint(self):
        print("Sub Class")

def main():
    myclass = subclass() #WRİTE SUBCLASS
    override = Overriding() #WRITE OVERRIDING

    myclass.print()#WRITE SUPERCLASS
    myclass.anotherprint()

    override.print()

if __name__ == '__main__':
    main()