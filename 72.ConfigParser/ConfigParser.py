#Author: Burak Dogancay
import configparser
import os

def getSpecFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName

def createConfigFile():
    global config
    config = configparser.ConfigParser()
    config['settings'] = {'resolution':'640x480', 'color' : 'blue', 'definition' : 'An image is something'}
    config['Image'] = {'BackgroundColor' : 'Black', 'ForegroundColor':'White'}
    
    with open(getSpecFile('settings.ini'),"w") as configFile:
        config.write(configFile)
        
def configFileBasicUsage():
    config.read(getSpecFile("settings.ini"))
    resolution = config.get("settings","resolution")
    foregroundColor = config.get("Image","BackgroundColor")
    
    print(resolution)
    print(foregroundColor)
    
    
def main():
    createConfigFile()
    configFileBasicUsage()


if __name__ == '__main__':
    main()
