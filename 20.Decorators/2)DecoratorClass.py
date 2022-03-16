from types import MethodType
#Author: Burak Dogancay
""" As mentioned in the introduction, a decorator is a function that can be applied to another function to augment its
behavior. The syntactic sugar is equivalent to the following: my_func = decorator(my_func). But what if the
decorator was instead a class? The syntax would still work, except that now my_func gets replaced with an instance
of the decorator class. If this class implements the __call__() magic method, then it would still be possible to use
my_func as if it was a function: """
#DECORATOR CLASS EXAMPLE
class Decorator(object):
    def __init__(self, func):
        self.func = func
        self.variable = ""
        self.variable2 = ""

    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():#real_function = Decorator(real_function)
    print('Inside the function.')
#-------------------------------

#SECOND DECORATOR CLASS EXAMPLE
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Inside the decorator.')
        return self.func(*args, **kwargs)
    def __get__(self, instance, cls):
    # Return a Method if it is called on an instance
        return self if instance is None else MethodType(self, instance)

class Test(object):
    @Decorator
    def __init__(self):
        self.var1 = " "
        self.var2 = " "
        pass
#-------------------------------

def main():
    
    #DECORATOR CLASS EXAMPLE
    myClass = Decorator(testfunc())
    myClass.variable = "First variable"
    myClass.variable2 = "SecondaVariable"
    print(myClass.variable)
    print(myClass.variable2)
    print("---------------------")
    print(testfunc())
    print("---------------------")
    #-------------------------------
    
    #SECOND DECORATOR CLASS EXAMPLE
    #Class Decorators only produce one instance for a specific function so decorating a method with a class decorator
    #will share the same decorator between all instances of that class:
    myClass2 = Test()
    myClass2.var1 = "First Variable"
    myClass2.var2 = "Seconda Variable"
    print(myClass2.var1)
    print(myClass2.var2)
    print("---------------------")
    #-------------------------------
    
if __name__ == '__main__':
    main()
