# Author: Burak Dogancay
#This module is used for keyboard and mouse control.İt automates mouseclick and keyboard press tasks.
#install this module using pip as : "pip install pyautogui"
from numpy import size
import pyautogui as pyGui

def exampleInfoFuncts():
    scrSize = pyGui.size()
    scrPos = pyGui.position()
    scrActWindow = pyGui.getActiveWindow()
    scrTitles = pyGui.getAllTitles()
    scrActTitle = pyGui.getActiveWindowTitle()
    print("--SCREEN INFORMATION--")
    print("Size of the Screen:",scrSize)
    print("Position of the mouse:",scrPos)
    print("Activated Windows:", scrActWindow)
    print("Get All Scr Titles :",scrTitles[3])
    print("Get Active Title : ", scrActTitle)
    print("---------------------")
   
def mouseFunctions():
    pyGui.moveTo(200,0,duration=2) # Move to this position
    pyGui.moveRel() #Move the cursor relative to current position
    pyGui.click(337,46) #it will
    pyGui.dragRel() #Mouse drag
    print("--MOUSE INFORMATION--")
    #print("Current Mouse Position:", pyGui.displayMousePosition())
    print("---------------------")

def keyboardFunctions():
    #pyGui.typewrite('')
    #pyGui.typewrite(['a','b','left'])#write given characters
    #pyGui.hotkey('ctrl','c')# combine two key
    #pyGui.hotkey('ctrl','v')
    print("--KEYBOARD KEYS--")
    print("Keyboard Keys Are:", pyGui.KEYBOARD_KEYS)
    print("---------------------")
    
    
    
def main():
   exampleInfoFuncts()
   mouseFunctions()
   keyboardFunctions()
    

if __name__ == '__main__':
    main()