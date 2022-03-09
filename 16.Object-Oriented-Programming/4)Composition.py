#Author: Burak Dogancay
class rocket():
    def print(self):
        print('Super class')

class compositionclass():
    def __init__(self):
        self.rocket = rocket()

    def anotherprint(self):
        print("Sub Class")

def main():
    myclass = compositionclass()

    myclass.rocket.print()
    myclass.anotherprint()

if __name__ == '__main__':
    main()