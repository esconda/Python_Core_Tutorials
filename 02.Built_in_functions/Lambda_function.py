#Author: Burak Dogancay
def lambdaFunctionEx(n):
    return lambda x : x+n

def main():

    Lambda_function = lambda x : x*x #It is like Define method in c++ after expression "x" assign it to other operation like "x*x".
    Lambdafunction2 = lambdaFunctionEx(20)

    print("Lambda Function Multiply", Lambda_function(20))
    print("Lambda Function Sum", Lambdafunction2(20))

if __name__=='__main__':
    main()