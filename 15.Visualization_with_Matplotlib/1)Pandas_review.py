import pandas as pd
import matplotlib as plot
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

    #Pandas basic methods
    dictionary = {"NAME": ["ali","kenan","veli","hilal","ayse","osman"], "AGE" :[15,20,30,40,60,70], "MAAS" :[100,150,200,250,300,350]}

    #SEEMS LIKE EXCEL VİEW
    dataframe1 = pd.DataFrame(dictionary)

    # Converts and save Datframe to csv
    dataframe1.to_json('iris1.csv')

    #Converts and save dataframe to json
    dataframe1.to_json('iris1.json')

    #read from csv file
    csv_info = pd.read_csv('iris.csv')
    get_columns_csv = csv_info.columns

    #read from json file
    json_info = pd.read_json('iris1.json')
    get_columns_json = json_info.columns
    print("inside of json",json_info)
    print("columns of json", get_columns_json)
    print("get age of json", json_info.AGE[1])

    print('csv : ', csv_info)
    print("columns of the cs files :", get_columns_csv)
    print("get values of specified column :\n", csv_info.variety)
    print("Get unique labels in csv files:\n", csv_info.variety.unique())
    #print("\n \n Info of the values:\n", csv_info.info())

    # Get specific columns
    setosa = csv_info[csv_info.variety == 'setosa'] # get values if it is equal to setosa
    virginica = csv_info[csv_info.variety == 'virginica']
    print("Get setosa elements:\n", setosa)
    print("Get virginica elements:\n", virginica)

    print("\ndescribe setosa values:\n", setosa.describe())
    print("describe virginica values:\n", virginica.describe())


if __name__=='__main__':
    main()