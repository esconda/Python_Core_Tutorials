import os
#Author: Burak Dogancay
#user defined functions
def myfunction(var1,var2):
    output = (((var1*var2)*50)/100)*var1/var2
    return output

#default function
def default_circle_area_calc(r, pi = 3.14): # pi value is for default function, default parametreler herzaman sona yazılır
    output = 2*pi*r
    return output

#flexible function
def flex_default_calc(height ,weight,*args,soyisim = "burak"):
    print("length of the arguments :",len(args))
    print("write name more than one :", args[0]*soyisim) #if you multiply string with integer, it writes multiple string
    print("Arguments", args)
    output = (height*weight)*args[0]*args[1] # get argument elements
    return output
# def flex_default_calc(height ,weight, age):
#     output = (height*weight)*age
#     return output

#Lambda Functions(Amacı daha hızlı bir şekilde fonksiyon yazabilmek)
def calculation(x):
    output = x*x
    return output


def main():

    mystring = "deneme"
    strtoint = "2700"
    integervalue = 10
    floatvalue = 10.4

    print("all libraries in os : ",dir(os))
    print("round float value : ",round(floatvalue))
    print("show type of the integer variable : ", type(integervalue))
    print("show type of the string variable : ", type(mystring))
    print("convert string to integer :", int(strtoint))

    #user defined function
    var1 = 10
    var2 = 100
    output = myfunction(var1, var2)#Call function for output calculation
    print("Output of the calculation is :", output)

    #default functions
    areaout = default_circle_area_calc(7)
    print("Area out", areaout)

    #flexible functions
    flex_areaout = flex_default_calc(20,30,5,6)
    print("flexible function calculation : ", flex_areaout)

    #Lambda functions
    output_not_lambda = calculation(20)# this is not lambda function, it is normal function
    output_lambda = lambda x : x*x #Here we have lambda function which is faster than normal function
    print("Lambda function is faster as above : ", output_lambda(20))


if __name__=='__main__':
    main()