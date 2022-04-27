# Author: Burak Dogancay
import pandas as pd
import csv
import os

def getSpecFile(pFileName):
  location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
  fileName= os.path.join(location,pFileName)#add file name to folder location
  return fileName

def readingWritingFunc():
  #WRITING CSV FİLE
  myDict = {'Baykar': ("Tb2", "Akinci"), 'Tai': ("Anka","Aksungur") , 'FNSS': ("Pars","Kaplan")}
  dataFrame = pd.DataFrame.from_dict(myDict, orient="index")
  dataFrame.to_csv(getSpecFile("data.csv"))
  
  #READING CSV FILE
  dataframe2 = pd.read_csv(getSpecFile("data.csv"))
  dictionary = dataframe2.to_dict()
  print("--User Defined Methodes--")
  print(dictionary)
  print("-----------------------")
  
def writingTsvFile():
  with open(getSpecFile("output.tsv"), 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['name', 'field'])
    tsv_writer.writerow(['Dijkstra', 'Computer Science'])
    tsv_writer.writerow(['Shelah', 'Math'])
    tsv_writer.writerow(['Aumann', 'Economic Sciences'])

def csvWriter():
  data = ["first_name,last_name,age".split(","),
          "Burak,Dogancay,32".split(","),
          "Yunus Emre,Tusun,31".split(","),
          "Melih,Mete,27".split(",")
      ] 
  #Open CSV file whose path we passed.
  with open(getSpecFile("anotherData.csv"), "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in data:
      print(line)
      writer.writerow(line)
  
  
def main():
  readingWritingFunc()
  writingTsvFile()
  csvWriter()


if __name__ == '__main__':
    main()