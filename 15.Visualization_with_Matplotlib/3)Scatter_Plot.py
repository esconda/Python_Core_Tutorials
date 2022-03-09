import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Author: Burak Dogancay

def main():


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
    plt.scatter(setosa.petal_length, setosa.petal_width, color ='red', label = "setosa")
    plt.scatter(virginica.petal_length, virginica.petal_width, color='green', label="virginica")
    plt.scatter(versicolor.petal_length, versicolor.petal_width, color='blue', label="versicolor")
    plt.legend()#it is for showing labels
    plt.xlabel("Petal-Length")
    plt.ylabel("Petal-Width")
    plt.title("Scatter-Plot")
    plt.show()

    # #print grid in the graph
    # csv_info.plot(grid = True)
    # plt.show()


if __name__ == '__main__':
    main()