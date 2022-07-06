from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
#Author: Burak Dogancay

def getFile(pFileName):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
    fileName= os.path.join(location,pFileName)#add file name to folder location
    return fileName

def main():
    # 1) pandas fast and efficient for dataframes
    # 2) We can open and examine csv and text files and save the results to these file types easily
    # 3) pandas makes our job easier for missing NAN data
    # 4) We can reshape and use data more effectively
    # 5) Slicing and indexing easy
    # 6) Help with time series data analysis
    # 7) Above all speed is a fast library with pandas optimized

    #read from csv file  
    csv_info = pd.read_csv(getFile('iris.csv'))

    #Convert pandas to numpy array
    numpyversionzeros = np.zeros((150,5))
    numpyversionzeros = np.array(csv_info)

    print("Numpy array version of csv file \n",numpyversionzeros)
    # Get specific columns
    setosa = csv_info[csv_info.species == 'setosa'] # get values if it is equal to setosa
    virginica = csv_info[csv_info.species == 'virginica']
    versicolor = csv_info[csv_info.species == 'versicolor']

    print("Read csv file ", csv_info)
    print("Get setosa elements:\n", setosa)
    print("Get virginica elements:\n", virginica)
    print("Get versicolor elements:\n", versicolor)

    print("\ndescribe setosa values:\n", setosa.describe())
    print("describe virginica values:\n", virginica.describe())


    #Plotting datafrmae directly
    #csv_info.plot()


    #Ploting detaily
    plt.plot([i for i in range(len(setosa.petal_length))],setosa.petal_length, color = "red" , label = "Setosa - Petal-Length")
    plt.plot([i for i in range(len(versicolor.petal_length))], versicolor.petal_length, color = "blue", label = "Versicolor - Petal_Length")
    plt.plot([i for i in range(len(virginica.petal_length))], virginica.petal_length, color="green",label="Virginica - Petal_Length")
    plt.xlabel("Id")
    plt.ylabel("Petal Length")
    plt.title("Show all type of iris")
    plt.legend()# it puts all elemnts in the graph
    plt.grid(True, linestyle = "--", alpha = 0.5) #draw grid in the graph
    plt.show()

    #Scatter Plot


    # #print grid in the graph
    # csv_info.plot(grid = True)
    # plt.show()







if __name__=='__main__':
    main()