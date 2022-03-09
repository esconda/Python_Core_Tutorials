import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Author: Burak Dogancay

def main():
    # 1) pandas fast and efficient for dataframes
    # 2) We can open and examine csv and text files and save the results to these file types easily
    # 3) pandas makes our job easier for missing NAN data
    # 4) We can reshape and use data more effectively
    # 5) Slicing and indexing easy
    # 6) Help with time series data analysis
    # 7) Above all speed is a fast library with pandas optimized

    # read from csv file
    csv_info = pd.read_csv('iris.csv')

    # Get specific columns
    setosa = csv_info[csv_info.species == 'setosa']  # get values if it is equal to setosa
    virginica = csv_info[csv_info.species == 'virginica']
    versicolor = csv_info[csv_info.species == 'versicolor']

    # Scatter Plot
    # csv_info.plot(grid=True, alpha = 0.9, subplots = True)
    # plt.show()

    #Alternative subplot
    plt.subplot(2,1,1) # iki tane subplotun birincisinin birincisi
    plt.plot([i for i in range(len(setosa.petal_length))], setosa.petal_length, color="red",label="Setosa - Petal-Length")
    plt.ylabel("setosa-Petallength")

    plt.subplot(2,1,2)
    plt.plot([i for i in range(len(versicolor.petal_length))], versicolor.petal_length, color="blue",label="Versicolor - Petal_Length")
    plt.ylabel("Versicolor-Petallength")
    plt.show()


if __name__ == '__main__':
    main()