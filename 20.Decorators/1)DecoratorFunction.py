#Author: Burak Dogancay

def secret_function(func):
    return func

@secret_function #my_functiont = super_secret_function(my_function)
def real_function():
    varList=["TB2","AKINCI","MIUS"]
    print("Variable List : ",varList)
    print("---------------------")
    
def main():
    secret_function
    
if __name__ == '__main__':
    main()
