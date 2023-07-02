import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def assign_Genre_values(df):
    p_values=df.to_list()

    p_values=list(set(p_values))

    #map the genre with key value.
    dictionary={}
    count=0
    for value in p_values:
        dictionary[value]=count
        count+=1
    
    # convrt dataframe to numerical value
    for index in range(0,df.shape[0]):
        try:
            if df[index] in dict.keys(dictionary):
                df[index]=dictionary[df[index]]
        except:
            pass
    return df

def construct_proper_dataframe():
    df=pd.read_csv('Dataset.csv')
    df.columns=['Movie','P_Genre','S_Genre','T_Genre']
    df['Movie']=df['Movie'].str.lower()

    #remove duplicaes
    df.drop_duplicates(subset ="Movie",keep='first',inplace=True)
    df['Movie']=df['Movie'].str.replace("  "," ")

    #feature selection, we select P_Genre, S_Genre and T_Genre as movie features
    df=df.reset_index(inplace=False)
    Genres=['P_Genre','S_Genre','T_Genre']
    for Genre in Genres:
        df[Genre]=assign_Genre_values(df[Genre])
    
    return df

def pre_process_all():
    df=pd.DataFrame()
    df=construct_proper_dataframe()
    #print(df.head(50))
    #print(df)
    # for item in df:
    #     print(item)
    return df



# pre_process_all()