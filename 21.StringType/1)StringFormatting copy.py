#Author: Burak Dogancay
#It covers changes made to existing string type variables.We can say that the string type variables are important in Python base to consider information details .

def basic_String_Formatting():
    float_Type = 25.4
    int_Type = 20
    str_Type = "String"
    
    #Formatiing output can be dteailed using str.format
    print('{} , {} and {}'.format(float_Type,int_Type,str_Type))
    print("---------------------")
    
    #Indexes can also be specified inside the brackets. The numbers correspond to indexes of the arguments passed to
    #the str.format function (0-based).
    print('{0}, {1}, {2}, and {1}'.format(float_Type, int_Type, str_Type))
    print("---------------------")
    
    #Named arguments can be also used:
    print("X value is: {first_val}. Y value is: {first_val}.".format(first_val=2, second_val=3))
    print("---------------------")
    
    #Dictionary
    my_dict = {'uav1': "tb2", 'uav2':"anka"}
    print("Uavs1 is : {0[uav1]}".format(my_dict)) # "0" is optional
    print("Uavs1 is : {0[uav2]}".format(my_dict))
    print("---------------------")
    
    #List
    my_list = ['tb2', 'akinci', 'mius']
    print("Third element of uav is: {0[2]}".format(my_list)) # "0" is optional
    print("---------------------")
    
    #Tuple
    t = (10, 3, 5, 12, 6)
    print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t))
    print("---------------------")
#Format Literals
#Literal format strings were introduced in PEP 498 (Python3.6 and upwards), allowing you to prepend f to the
#beginning of a string literal to effectively apply .format to it with all variables in the current scope
def format_Litearls():
    uav = "tb2"
    print('Uav is {}'.format(uav))
    print("---------------------")

#Float Formatting
def float_Formatting():
    print("Float Formatting")
    print('{0:.0f}'.format(24.12345))
    print('{0:.1f}'.format(24.12345))
    print('{0:.5f}'.format(24.12345))
    print('{0:.7f}'.format(24.12345))
    print("---------------------")
    
   #Floating point numbers can also be formatted in scientific notation or as percentages
    print('{0:.3e}'.format(24.12345))
    print('{0:.0%}'.format(24.12345))
    print("---------------------")

def named_Placeholders():
    print("Named Place Holders")
    carData = {'Honda': 'Civic', 'Bmw': 'f30'}
    print('{Honda} {Bmw}'.format_map(carData))
    print("---------------------")
    
def numeric_Values_Formatting():
    print("Numerical Formatting")
    print('{:c}'.format(65))
    print('{:d}'.format(0x0a))
    print('{0:x}'.format(10))
    print('{0:X}'.format(10))
    print('{:o}'.format(10))
    print('{:b}'.format(10))
    print("---------------------")
    
    r, g, b = (1.0, 0.4, 0.0)
    print('#{:02X}{:02X}{:02X}'.format(int(255 * r), int(255 * g), int(255 * b)))
    
def main():
    basic_String_Formatting()
    format_Litearls()
    float_Formatting()
    named_Placeholders()
    numeric_Values_Formatting()
    

if __name__ == '__main__':
    main()
