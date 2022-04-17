# Author: Burak Dogancay
import xml.etree.ElementTree as xml
import os

from sympy import root

def getSpecFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName
  
def openAndReadFunc():
  #Import Element Tree module and open xml file, get an xml element
  global baykarElement
  global taiElement
  
  tree = xml.parse(getSpecFile("UavData.xml"))
  rootTree = tree.getroot()
  
  baykarElement = rootTree[0]
  taiElement = rootTree[1]
  
  print("--MAİN UAV ELEMENTS--")
  print("Baykar Uav element name : ",baykarElement.attrib['name'])
  print("Tai Uav Element name : ",taiElement.attrib['name'])
  print("Baykar Uav element name : ",baykarElement.attrib['id'])
  print("Tai Uav Element name : ",taiElement.attrib['id'])
  
  print("Baykar Uav element name another methode : ",rootTree.find('./Bayraktar').attrib['name'])
  print("Tai Uav Element name another methode  : ",rootTree.find('./Tai').attrib['name'])
  print("Baykar Uav element name  another methode : ",rootTree.find('./Bayraktar').attrib['id'])
  print("Tai Uav Element name another methode : ",taiElement.attrib['id'])
  print("---------------------")  

def getAllElements():
  
  print("--BAYKAR UAV ELEMENTS--")
  for element in baykarElement:
    for subelement in element:
      print(subelement.text)
  print("---------------------") 
  
  print("--TAI UAV ELEMENTS--")
  for element in taiElement:
    for subelement in element:
      print(subelement.text)
  print("---------------------") 
  
def main():
  openAndReadFunc()
  getAllElements()

if __name__ == '__main__':
    main()