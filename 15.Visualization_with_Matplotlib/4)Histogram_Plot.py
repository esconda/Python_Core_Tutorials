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

    # Convert pandas to numpy array this just shows how to convert panda type to numpy type
    numpyversionzeros = np.zeros((150, 5))
    numpyversionzeros = np.array(csv_info)

    print("Numpy array version of csv file \n", numpyversionzeros)


    # Get specific columns
    setosa = csv_info[csv_info.species == 'setosa']  # get values if it is equal to setosa
    virginica = csv_info[csv_info.species == 'virginica']
    versicolor = csv_info[csv_info.species == 'versicolor']

    print("Get setosa elements:\n", setosa)
    print("Get virginica elements:\n", virginica)
    print("Get versicolor elements:\n", versicolor)

    # Scatter Plot
    plt.hist(setosa.petal_length, bins = 50)#Check how many same value available in the petal length of the setosa, 10 is th default graph view
    plt.xlabel("Numbers")
    plt.ylabel("How many same numbers available")
    plt.title("Histogram")
    plt.show()
    # #print grid in the graph
    # csv_info.plot(grid = True)
    # plt.show()

if __name__ == '__main__':
    main()