#Author: Burak Dogancay
import math
from tkinter.tix import TCL_ALL_EVENTS

def roundingFunctions():
    #Math module provide math module of floor,ceil,trunc functions
    firstVar = 25.5
    secondVar = 20.1
    
    roundVar = round(20)
    floorVar = math.floor(firstVar+secondVar)
    ceilVar = math.ceil(firstVar+secondVar)
    truncVar = math.trunc(firstVar+secondVar)
    
    print("ROUNDING OPERATIONS")
    print(" Round Variable : ", roundVar)
    print(" Floor Variable : ", floorVar)
    print(" Ceil Variable : ", ceilVar)
    print(" Truncated Variable : ", truncVar)
    print("---------------------")

def trigonometricFunctions():
    
    #Hypotenuse
    hypotenuseVar = math.hypot(3,4)
    
    #Degrees and Radians conversion
    degreesVar = math.degrees(math.asin(1)) #Convert to degrees
    radianVar = math.radians(90) #Conevrt to radian
    
    #Sine,Cosine,tangent and inverse functions
    sineVar = math.sin(math.pi / 4)
    asinVar = math.asin(1)
    cosVar = math.cos(math.pi / 2)
    acosVar = math.acos(1)
    tanVar = math.tan(math.pi/4)
    atanVar = math.atan(math.inf)
    
    print("TRIGONOMETRIC OPERATIONS")
    print(" Hypotenuse Variable : ", hypotenuseVar)
    print(" Degrees Variable : ", degreesVar)
    print(" Radian Variable : ", radianVar)
    print(" Sine Variable : ", sineVar)
    print(" Asine Variable : ", asinVar)
    print(" Cosine Variable : ", cosVar)
    print(" Acos Variable : ", acosVar)
    print(" Tan Variable : ", tanVar)
    print(" Atan Variable : ", atanVar)
    print("---------------------")

def fastestPowFunc():
    powVar = math.pow(5,3)
    print("POW OPERATION")
    print(" Pow Variable : ", powVar)
    print("---------------------")
    
def logarithmFunc():
    firstVar = math.log(math.e)
    secondVar = math.log(1)
    log10Var = math.log(10)
     
    print("LOGARITHM OPERATIONS")
    print(" First Variable : ", firstVar)
    print(" Second Variable : ", secondVar)
    print(" Logarithm10 Variable : ", log10Var)
    print("---------------------")
    
def constants():
    eVar = math.e
    piVar = math.pi
    infVar = math.inf
    
    print("CONSTANT OPERATIONS")
    print(" E Variable : ", eVar)
    print(" Pi Variable : ", piVar)
    print(" inf Variable : ", infVar)
    print("---------------------")

def copyingSigns():
    #math.copysign(x, y) returns x with the sign of y. The returned value is always a float
    math.copysign(-2, 3) # 2.0
    math.copysign(3, -3) # -3.0
    math.copysign(4, 14.2) # 4.0
    math.copysign(1, -0.0) # -1.0, on a platform which supports signed zero
    
def main():
    roundingFunctions()
    trigonometricFunctions()
    fastestPowFunc()
    logarithmFunc()
    constants()
    copyingSigns()
if __name__ == '__main__':
    main()
