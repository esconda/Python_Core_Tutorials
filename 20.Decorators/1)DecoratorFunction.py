#Author: Burak Dogancay

#DECORATOR FUNCTION EXAMPLE
def secret_function(func):
    print("Decorable Function")
    return func

@secret_function #real_function = super_secret_function(real_function)
def real_function():
    varList=["TB2","AKINCI","MIUS"]
    print("Variable List : ",varList)
    print("---------------------")
#-------------------------------

#ANOTHER DECORATOR EXAMPLE
def print_args(func):
    def inner_func(*args, **kwargs):
        print("Arguments : ",args)
        print("Keywords : ",kwargs)
        print("---------------------")
        return func(*args, **kwargs) #Call the original function with its arguments.
    return inner_func

@print_args 
def multiply(num_a, num_b):
    return num_a * num_b 
#-------------------------------

def main():
    real_function()
    
if __name__ == '__main__':
    main()
