# Author: Burak Dogancay
#WILL BE CONTİNUED LATER
import PIL as pillow
from PIL import Image,ImageColor,ImageShow,ImageFont,ImageDraw
import os
import time

def getSpecFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName

def getFileName(pFileLocFileName):
  manipulateFile = pFileLocFileName
  file = os.path.splitext(manipulateFile)
  return file[0]

def readingImage():
  image = Image.open(getSpecFile("tb2.jpg"))
  image.show()
  image.close()
  
def convertFileToJpg(): ##Wont work will be corrected later
  inFile = getSpecFile("PillowText.txt")
  outFile = getFileName(inFile)+".jpg"
  if inFile != outFile:
    try:
      image = Image.open(inFile)
      image.save(outFile)
    except IOError:
      print("Can not convert :", inFile)
      
def main(): 
  readingImage()
  convertFileToJpg()
 
if __name__ == '__main__':
    main()