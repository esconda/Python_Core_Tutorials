import pandas as pd
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

    # Pandas basic methods
    dictionary = {"NAME": ["ali", "kenan", "veli", "hilal", "ayse", "osman"], "AGE": [15, 20, 30, 40, 60, 70],
                  "SALARY": [100, 150, 200, 250, 300, 350]}
    print("Dictionary without pandas dataframe view :", dictionary)

    # SEEMS LIKE EXCEL VİEW
    dataframe1 = pd.DataFrame(dictionary)

    # Average salary with panda dataframe
    mean_value_pd = dataframe1.SALARY.mean()  # average salary
    print("Average Salary :", mean_value_pd)

    # Average salary with numpy
    mean_value_np = np.mean(dataframe1.SALARY)
    print("Average Salary Numpy :", mean_value_np)

    # LIST COMPREHENSION
    dataframe1["Salary_Level"] = ["dusuk" if mean_value_pd > each else "yuksek" for each in
                                   dataframe1.SALARY]  # this one is equal to belov one
    print(dataframe1, "\n")
    # -----------------------------------

    #drop and concatenating

    #DROP
    dataframe1 = dataframe1.drop(["Salary_Level"],axis=1)#axis 0 satır drop, axis 1 sütun drop
    print("dropped : \n", dataframe1)
    #---------------------

    #CONCATENATE
    data1 = dataframe1.head()
    data2 = dataframe1.tail()

    #vertical concatenation
    data_concat = pd.concat([data1,data2], axis = 0)

    dataframe1["list_comp"] = [each*2 for each in dataframe1.AGE]#MULTİPLY EACH VALUE AGE OF DATAFRAME

    #Apply()
    dataframe1["apply_method"] = dataframe1.AGE.apply(multiply)
    print(dataframe1)

def multiply(AGE):
    return AGE*2

if __name__ == '__main__':
    main()