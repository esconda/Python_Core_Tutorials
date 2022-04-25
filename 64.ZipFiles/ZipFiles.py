# Author: Burak Dogancay
import os
from zipfile import ZipFile

def getSpecFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName

def zipFileContents():
    with ZipFile(getSpecFile('UavData.zip'),'r') as zip:
        zip.printdir() # gives information about zipfile
        zip.close() # close the zip file
        
    with ZipFile(getSpecFile('64.ZipFiles.zip'),'r') as zip:
        info = zip.infolist()
        namelist = zip.namelist()
        
        print("--ZIP PROPERTIES--")
        print("List of the Archieve : ",namelist)
        print("Info of the list : ",info)
        print("-------------------")
        zip.close()
        
def openZipFile():
    zip = ZipFile(getSpecFile('64.ZipFiles.zip'))
    print(zip)
    zip.close()
    
def createNewArchieves():
    archieve = ZipFile(getSpecFile('newArchieve.zip'),mode = 'w')
    
    #Add files to archieve
    archieve.write(getSpecFile("data.csv"),"Data.csv") # firstfile to be zipped
    archieve.write(getSpecFile("uavData.xml"),"UnmannedVehicleData.xml") #second file to be zipped
    archieve.close()
    
def extractingZipFile():
    zipFile = ZipFile(getSpecFile("newArchieve.zip"))
    zipFile.extractall(getSpecFile("Extracteditems"))
    zipFile.close()
    
def extractingPartFile():
    f=open(getSpecFile("newArchieve.zip"),'rb')
    zfile=ZipFile(f)
    zfile.extract(zfile.namelist()[1],getSpecFile("ExtractPartFile"))
    
def main():
    zipFileContents()
    openZipFile()
    createNewArchieves()
    extractingZipFile()
    extractingPartFile()
    

if __name__ == '__main__':
    main()