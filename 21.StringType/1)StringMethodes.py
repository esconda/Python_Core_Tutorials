#Author: Burak Dogancay

import string


def strMethods():
    strVar = "this is my string"
    casefoldStr = strVar.casefold() #str.casefold creates a lowercase string that is suitable for case insensitive comparisons
    capitalStr = strVar.capitalize() #Capitalizes first character
    upperStr = strVar.upper()#Capitalize all characters
    lowerStr = strVar.lower()#Lower case representation of the string
    titleStr = strVar.title()#str.title returns the title cased version of the string
    swapCaseStr = strVar.swapcase() #str.swapcase returns a new string object in which all lower case characters are swapped to upper case and all upper case characters to lower
    
    print("STRING METHODES")
    print("Creates lower case string : ",casefoldStr)
    print("Capitalize first character : ",capitalStr)
    print("Upper string : ",upperStr)
    print("Lower string : ",lowerStr)
    print("Title of the string : ",titleStr)
    print("Swap case of the string : ",swapCaseStr)
    print("---------------------")
    
def translateCharacters():
    #Python supports a translate method on the str type which allows you to specify the translation table (used for replacements) as well as any characters which should be deleted in the process.
    strVar = "Translate String"
    translationTableStr = str.maketrans("aei", "231")
    translatedStr = strVar.translate(translationTableStr)
    
    print("STRING TRANSLATION METHODE")
    print("Translated stirng is : ",translatedStr)
    print("---------------------")
    
def stringModule():
    strLetters = string.ascii_letters
    strLowercase = string.ascii_lowercase
    strUppercase = string.ascii_uppercase
    
    print("STRING MODULE")
    print("Ascii Letters : ",strLetters)
    print("Ascii Letters Lowercase : ",strLowercase)
    print("Ascii Letters Uppercase : ",strUppercase)
    print("---------------------")

def stripUnwantedChr():
    #Strip unwanted character in defined string
    strVar = "The best car is my Anadol"
    strippedChr = strVar.strip("Anadol")
        
    print("STRING STRIP MODULE")
    print("Stripped string :",strippedChr)
    print("---------------------")
    
def reverseString():
    strVar = "The best car is my Anadol"
    #First Methode
    reversedStr = ''.join(reversed(strVar))
    
    #Second Methode
    reversedStr2 = strVar[::-1]
    
    print("STRING REVERSE METHODE")
    print("Reversed string :",reversedStr)
    print("Reversed string 2 :",reversedStr2)
    print("---------------------")

def splitString():
    #String splitting
    strVar = "The best car is my Anadol"
    strSplit = strVar.split()
    maxSplit = strVar.split(' ',maxsplit=0)#the maxsplit parameter limits the number of splittings that occur
    strSplit2 = strVar.split("e")
    
    
    print("STRING SPLIT METHODE")
    print("Split string :",strSplit)
    print("Max split string :",strSplit)
    print("Split string by e :",strSplit2)
    print("---------------------")
    
def replaceChr():
    #This is the mothode of replacing any word or character ins the string
    strVar = "The best car is my Anadol"
    replacedStr = strVar.replace("Anadol", "Bmw")
    
    print("STRING REPLACE METHODE")
    print("Replaced character of the string :",replacedStr)
    print("---------------------")
    
def joinMethode():
    strVar = "The best car is my Anadol"
    joinedStr = strVar.join(["Unfortunately it is a joke"])
    
    print("STRING JOIN METHODE")
    print("Join string to string :",joinedStr)
    print("---------------------")
    
def countNumberInStr():
    strVar = "The best car is my Anadol"
    countWordtInStr = strVar.count("best")
    countChrInStr = strVar.count("e")
    
    print("STRING COUNTING NUMBER OF SUBSTRING IN METHODE")
    print("Counting number of times a substring appearsin a string :",countWordtInStr)
    print("Counting number of times a char appears in a string :",countChrInStr)
    print("---------------------")
    
    
def main():
  strMethods()
  translateCharacters()
  stringModule()
  stripUnwantedChr()
  reverseString()
  splitString()
  replaceChr()
  joinMethode()
  countNumberInStr()
    

if __name__ == '__main__':
    main()
