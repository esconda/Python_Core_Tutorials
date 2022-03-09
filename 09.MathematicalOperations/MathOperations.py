from enum import Enum
#Author: Burak Dogancay
import operator
import math

def main():
    a = 3
    b = 2

    #Division
    print("Division : ",operator.truediv(a, b))  # = 1.5
    print("Division Alternative : ",operator.truediv(a, b))  # = 1.5
    print("Division Alternative 1 : ",operator.floordiv(a,b)) # =1
    print("Division Alternative 2 : ", a//b) # =1

    #Addition
    print("Addition : ",operator.add(a,b)) # =5
    print("Addition Alternative :",a+b) #=5

    #Exponentiation
    print("Exponentiation : ", operator.pow(a, b))  # =9
    print("Exponentiation Alternative :", a ** b)  # =9
    print("Exponentiation Alternative 1", math.pow(a,b)) #=9.0

    #Square Root
    print("Square Root : ", math.sqrt(a))  # =1.73

    #Subtraction
    print("Subtraction : ", operator.sub(a,b))  # =1
    print("Subtraction Alternative : ", a-b) # =1

    #Multiplication
    print("Multiplication : ", operator.mul(a, b))  # =6
    print("Multiplication Alternative : ", a * b)  # =6

    # Modulus
    print("Modulus : ", operator.mod(a, b))  # =1
    print("Modulus Alternative : ", a % b)  # =1

    #TRIGONOMETRİC FUNCTIONS
    c,d = 1,2
    print("Sinus : ",math.sin(c))  # returns the sine of 'a' in radians
    # Out: 0.8414709848078965
    print("Cosinus : ",math.cosh(d))  # returns the inverse hyperbolic cosine of 'b' in radians
    # Out: 3.7621956910836314
    print("Arch Tanjent : ",math.atan(math.pi))  # returns the arc tangent of 'pi' in radians
    # Out: 1.2626272556789115
    print("Hypot : ", math.hypot(c, d))  # returns the Euclidean norm, same as math.sqrt(a*a + b*b)
    # Out: 2.23606797749979
    print("Radian to Degree",math.degrees(c))
    # Out: 57.29577951308232
    print("Degree to Radian", math.radians(57.29577951308232))
    # Out: 1.0
    print("Logarithms : ", math.log(math.pi))  # returns the logarithm
    # Out: 1.1447

    #Inplace Operations
    e = 5

    e = e+1
    print(a + 1)

    e = e * 2
    print(e)

    e+=1
    print(e)

    e*=2
    print(e)

if __name__=='__main__':
    main()