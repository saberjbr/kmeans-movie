import clustering
import os


def recommand_movie():
    input_movie=input("Enter a Movie Name: ")
    try:
        os.remove('ds_temp.csv')
    except:
        pass
    movies=clustering.cluster_everything(input_movie)
    if type(movies)==int:
        pass
    else:
        print(movies)   


    
    
recommand_movie()