# Author: Burak Dogancay
import xml.etree.ElementTree as xml
import os

from sympy import root

def getSpecFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName

def indendationOp(elem,level=0):
  #Arrange all indentation for xml file
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indendationOp(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def openAndReadFunc():
  #Import Element Tree module and open xml file, get an xml element
  global baykarElement
  global taiElement
  global rootTree
  
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
  
def otherFunc():
  #get element of Baykar
  #To search for specific tags by name, use the .find or .findall:
  elementBaykar = baykarElement[0]
  elementBaykar1 = baykarElement[0][0]
  print("--TAI UAV ELEMENTS--")
  print("Tag name is : ", elementBaykar1.tag)
  print("Text is : ", elementBaykar1.text)
  print("Uav type attributes:", elementBaykar.attrib)
  print("Uav Type first atribute :",elementBaykar.attrib["uniqId"])
  print("Find all elements : " , rootTree.findall('.//Name'))
  print("Find first name element : " , rootTree.find('.//Name').text)
  print("---------------------") 
  
def createXmlElement():
  #Element() function is used to create XML elements
  main=xml.Element('parent')
  
  #SubElement() function used to create sub-elements to a give element
  sub1 = xml.SubElement(main, 'child1')
  sub2 = xml.SubElement(main, 'child2')
  sub3 = xml.SubElement(main, 'child3')
  
  #Add attributes to child element
  sub1.attrib = {"Name" : "First Element"}
  sub2.attrib = {"Name" : "Second Element"}
  sub3.attrib = {"Name" : "Third Element"}
  
  #Add Text to childs
  sub1.text = "First Element text"
  sub2.text = "Second Element text"
  sub3.text = "Third Element text"
  
  #dump() function is used to dump xml elements.
  xml.dump(main)
  
  #saving xml
  rootTree = xml.ElementTree(main)
  indendationOp(main) # Arrange intendation
  rootTree.write(getSpecFile("Output.xml"),encoding="utf-8", xml_declaration=True)
  
  
  
def main():
  openAndReadFunc()
  getAllElements()
  otherFunc()
  createXmlElement()

if __name__ == '__main__':
    main()