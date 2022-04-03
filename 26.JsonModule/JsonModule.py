# Author: Burak Dogancay
import json
import os


def getFile(pFileName):
    location = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))  # it gets the folder location
    # add file name to folder location
    fileName = os.path.join(location, pFileName)
    return fileName


def storeDataInFile():
    # WRITE TO JSON FILE
    data = {
        'uav1': 'anka',
        'uav2': "tb2",
        'uav3': ["tb2", "anka", "akinci"]
    }

    with open(getFile("JSONDocument.json"), 'w') as file:
        json.dump(data, file)


def retrieveDataFromFile():
    # READ JSON FILE
    with open(getFile("JSONDocument.json"), 'r') as file:
        data = json.load(file)
    print("----JSON DATA----")
    print("Json Data is  : ", data)
    print("---------------------")


def formatJsonOutput():
    data = {
        'uav1': 'anka',
        'uav2': "tb2",
        'uav3': ["tb2", "anka", "akinci"]
    }

    with open(getFile("JSONDocument2.json"), 'w') as file:
        json_object = json.dumps(data, indent=4)  # this indetattion
        file.write(json_object)


def loadVsLoads():
    
    # Loads example can be used to deserialize str (s) instance containing a JSON document to a Python dictionary object
    data = """{ 
    "Name": "Burak Dogancay", 
    "Contact Number": 1234565, 
    "Email": "pm_brk@hotmail.com", 
    "Hobbies":["Coding", "Gaming", "Pumping :)"] 
    }"""
    
    dataLoads = json.loads(data) # Converts string to dictionary for json
    print("----JSON DATA LOADS----")
    print("Json Data is  : ", dataLoads)
    print("---------------------")
    
    #Create new json file and Dum dtataLoads dictionary
    with open(getFile("PersonalJsonFile.json"),'w') as json_file:
        json.dump(dataLoads,json_file)


    # Load Example
    with open(getFile("JSONDocument.json"), 'r') as file:
        data = json.load(file)
        print("----JSON DATA LOAD----")
        print("Json Data is  : ", data)
        print("---------------------")


def main():
    storeDataInFile()
    retrieveDataFromFile()
    formatJsonOutput()
    loadVsLoads()


if __name__ == '__main__':
    main()
