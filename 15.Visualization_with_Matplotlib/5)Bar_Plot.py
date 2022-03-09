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
    x = np.array([1,2,3,4,5,6,7])
    a = ["turkey","usa","a","b","c","d","e"]
    y = x*2+5

    # Scatter Plot
    plt.bar(a,y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Bar-Plot")
    plt.show()

    # #print grid in the graph
    # csv_info.plot(grid = True)
    # plt.show()


if __name__ == '__main__':
    main()