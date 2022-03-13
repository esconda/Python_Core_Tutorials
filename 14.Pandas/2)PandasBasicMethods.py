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
    dictionary = {"NAME" : ["ali","kenan","veli","hilal","ayse","osman"], "AGE" :[15,20,30,40,60,70], "SALARY" :[100,150,200,250,300,350]}

    #SEEMS LIKE EXCEL VİEW
    dataframe1 = pd.DataFrame(dictionary)

    print("Dataframe of the dictionary : \n", dataframe1)

    head = dataframe1.head(5) # get first 5 positions from beginning
    print("get first 5 positions from beginning \n", head)

    tail = dataframe1.tail(5) # get last 5 positions from end
    print("get last 5 positions from end : \n", tail)

    print("Get columns of the pandas dataframe : ", dataframe1.columns, "\n") #write coulmns of the dataframe
    print(dataframe1.info()) #information about dataframe1
    print(dataframe1.describe()) #get only numeric values

if __name__=='__main__':
    main()