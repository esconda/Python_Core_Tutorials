import pandas as pd
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
    dictionary = {"NAME" : ["ali","kenan","veli","hilal","ayse","osman"], "AGE" :[15,20,30,40,60,70], "MAAS" :[100,150,200,250,300,350]}
    print("Dictionary without pandas dataframe view :",dictionary)

    #SEEMS LIKE EXCEL VİEW
    dataframe1 = pd.DataFrame(dictionary)

    #FILTER VARIABLES FROM DATAFRAME
    filtre1 = dataframe1.MAAS >200
    filtered_data = dataframe1[filtre1]
    print("filtered data :", filtered_data)

    #FILTER SECOND CONDITION
    filtre2= dataframe1.AGE == 60
    filtered2_data = dataframe1[filtre2]
    print("filtered 2. data :", filtered2_data)

    #CHECK BOTH FILTERS
    print("filtered double find ayse suitable :", dataframe1[filtre1&filtre2])


if __name__=='__main__':
    main()