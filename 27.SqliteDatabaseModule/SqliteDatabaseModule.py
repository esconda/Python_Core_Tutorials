# Author: Burak Dogancay
import json
import os
import sqlite3
from enum import Enum

class UAV(Enum):
        Firm = 0
        Type = 1
        Name = 2
        Id = 3
def getFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))  # it gets the folder location
    # add file name to folder location
    fileName = os.path.join(location, pFileName)
    return fileName

def databaseFileEx1():
    #Dtabase connection
    conDatabase =  sqlite3.connect(getFile('ExDatabase.db'))
    cur = conDatabase.cursor()
    
    #Execute Sql Command
    cur.execute("SELECT * FROM UAV")
    
    #Read from Database
    for row in cur:
        print("--SELECT ITEM FROM TABLE--")
        print("Firm is : ", row[UAV.Firm.value])
        print("Type is : ", row[UAV.Type.value])
        print("Name is : ", row[UAV.Name.value])
        print("Id is : ", row[UAV.Name.value])
        print("---------------------")
    
    #Close Connection
    cur.close()

def databaseFileEx2():
    #Dtabase connection
    conDatabase =  sqlite3.connect(getFile('ExDatabase.db'))
    cur = conDatabase.cursor()
    
    #Execute Sql Command
    cur.execute("SELECT * FROM UAV")
        
    fetchOne=cur.fetchone()
    fetchMany=cur.fetchmany() #which is similar to list(cursor) method used previously
    fetchAll=cur.fetchall()
    
    #FETCH ONE
    print("--FETCH ONE--")
    for row in fetchOne:
        print (row)
    print("---------------------")
    
    #FETCH MANY
    print("--FETCH MANY--")
    for row in fetchMany:
        print (row)
    print("---------------------")
    
    #FETCH ALL
    print("--FETCH ALL--")
    for row in fetchAll:
        print (row)
    print("---------------------")
    
    
    #Close Connection
    cur.close()

def main():
    databaseFileEx1()
    databaseFileEx2()

if __name__ == '__main__':
    main()
