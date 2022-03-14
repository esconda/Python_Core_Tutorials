from fileinput import filename
from inspect import getfile
from math import factorial
import mmap
import os
from sympy import content
import shutil

#Author: Burak Dogancay
""" Functions in Python provide organized, reusable and modular code to perform a set of specific actions. Functions
simplify the coding process, prevent redundant logic, and make the code easier to follow. This topic describes the
declaration and utilization of functions in Python.
Python has many built-in functions like print(), input(), len(). Besides built-ins you can also create your own
functions to do more specific jobs—these are called user-defined functions. """
def simpleFunction():
    print("This is a simple function without arguments")
    print("---------------------")

def simpleFunctArg(arg="Default argument"):#here we define default argument for arg
    print("This is a simple function with argument : ", arg)
    print("---------------------")
    
def funcwithmanyArg(*args):
    print("Arbitrary Number of arguments")
    for i in args:
        print(i)
    print("---------------------")

def functwithkeyargs(**kwargs):
    print("Arbitrary Number of keyword arguments")
    for types,value in kwargs.items():
        print(types,value)
    print("---------------------")
    
def mixFunction(var = "Default var",*args,**kwargs):
    print("Mixed function with arguments")
    print("Variable is : ",var)
    for i in args:
        print(i)
        
    for types,value in kwargs.items():
        print(types,value)
    print("---------------------")

def optionalArg(action='nothing'):
    #Optional arguments can be defined by assigning (using =) a default value to the argument-name:
    print("Optional Argument is : ",action)
    print("---------------------")
    return action  
    
def lambdaFunct():
    lambdaEx = lambda: "Hello World"
    strip_and_upper_case = lambda str: str.strip().upper()#Lambda takes arguments "str"
    argsLambda = lambda x, *args, **kwargs:(x,args,kwargs) 
    sortWithLambda = sorted( [" foo ", " bAR", "BaZ "], key=lambda s: s.strip().upper())
    mapWithLambda = sorted( map( lambda s: s.strip().upper(), [" foo ", " bAR", "BaZ "]))
    
    #List with Lambda
    listWithLambda = [3, -4, -2, 5, 1, 7]
    opLambdaList = list( filter( lambda x: x>0, listWithLambda))
    opLambdaList1 = list( map( lambda x: abs(x), listWithLambda))
    opLambdaList2 = sorted( listWithLambda, key=lambda x: abs(x))
    
    #Recursive Lambda
    lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
    
    print("LambdaEx output : ", lambdaEx)
    print("Lambda with arguments : ",strip_and_upper_case("Strings") )
    print("Lambda with arguments and keyword arguments : ",argsLambda('hello', 'world', world='world'))
    print("Sorting with Lambda : ",sortWithLambda)
    print("Map with Lambda : ",mapWithLambda)
    print("List with Lambda : ",opLambdaList)
    print("List with Lambda : ",opLambdaList1)
    print("List with Lambda : ",opLambdaList2)
    print("Recursive Lambda:", lambda_factorial(4))
    print("---------------------")
    
def mutableFunction(passedList):
    #argument (actual parameter): the actual variable being passed to a function;
    #parameter (formal parameter): the receiving variable that is used in a function.
    #In Python, arguments are passed by assignment (as opposed to other languages, where arguments can be
    #passed by value/reference/pointer)
    #Immutable: Integers, strings, tuples, and so on. All operations make copies.
    #Mutable: Lists, dictionaries, sets, and so on. Operations may or may not mutate
    passedList[0] = 10
    print("Mutable var : ",passedList)
    print("---------------------")
    
def returnVarFunc(arg):
    print("Returned Function Variable : ",arg)
    print("---------------------")
    return arg

def closureFunct(x):
    #Closures in Python are created by function calls. Here, the call to makeInc creates a binding for x that is referenced
    #inside the function inc. Each call to makeInc creates a new instance of this function, but each instance has a link to a
    #different binding of x
    def inc(y):
        return y + x
    return inc

def nestedFunction(var):
    def fibonacci(n):
        def step(a,b):
            return b,a+b
        a,b = 0,1
        for i in range(n):
            a,b = step(a,b)
        return a
    fibonacci(var)

def recursiveFunctionsFact(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def main():
    #ABOUT FUNCTION ARGUMENTS
    #arg1, ..., argN Regular arguments
    #*args Unnamed positional arguments
    #kw1, ..., kwN Keyword-only arguments
    #**kwargs The rest of keyword arguments
    
    #Call Simple Function Without arguments
    simpleFunction()
    #----------------
    
    #Call Simple Function with Argument
    simpleFunctArg("My Argument")
    #----------------
    
    #Call function with many arguments
    funcwithmanyArg(1,2,3)
    
    myList = ["TB2","AKINCI","MIUS"]
    funcwithmanyArg(*myList)# Calling it with list of values, * expands the list
    #----------------
    
    #Call function with many keyword arguments
    functwithkeyargs(type1="TB2", type2="AKINCI", type3="MIUS")
    
    my_dict = {'car': "toyota", 'plane':"airbus"}
    functwithkeyargs(**my_dict)#Calling it with dictionary
    #----------------
    
    #Mixed function with arguments and keyword arguments
    var = "Defined Argument"
    myList_args = ["TB2","AKINCI","MIUS"]
    my_dict_keyargs = {'car': "toyota", 'plane':"airbus"}
    mixFunction(var,*myList_args,**my_dict_keyargs)
    #----------------
    
    #Defining a function with optional arguments
    optionalArg("Heyo")
    optionalArg(action="pofff")
    optionalArg()
    #----------------
    
    #Lambda Functions
    lambdaFunct()
    #----------------
    
    #Argument passing and mutability
    myList = [1,2,3,4,5]
    mutableFunction(myList)
    #----------------
    
    #Return Function Variable
    returnVarFunc(10)
    #----------------
    
    #Closure 
    closureFunct(30)
    #----------------
    
    #Nested Functions
    nestedFunction(5)
    #----------------
    
    #Recursive Functions
    recursiveFunctionsFact(15)
    #----------------
    

if __name__ == '__main__':
    main()
