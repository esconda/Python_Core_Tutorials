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
    print("Dictionary without pandas dataframe view :",dictionary)

    #SEEMS LIKE EXCEL VİEW
    dataframe1 = pd.DataFrame(dictionary)

    #INDEXING AND SLICING
    print("Name and Ages :",dataframe1["NAME"],dataframe1["AGE"])

    #ADD NEW INDEX AND FURURE TO PANDAS DATAFRAME
    dataframe1["new_future"] = [1,2,3,4,5,6]
    print("Add new future : ",dataframe1["new_future"])
    print("Restrict age index :",dataframe1.loc[:3,"AGE"])
    print("Another example : ", dataframe1.loc[:3, ["AGE","NAME"]])
    print(dataframe1.loc[:,:"SALARY"]) # PRİNT ALL VALUES UNTILL TO SALARY

    #REVERSING DATAFRAME
    print("reversing dataframe", dataframe1.loc[::-1,:])

if __name__=='__main__':
    main()