import clustering_code
import os


def get_movie_name():
    input_movie=input("Enter a Movie Name: ")
    try:
        os.remove('ds_temp.csv')
    except:
        pass
    movies=clustering_code.cluster_everything(input_movie)
    if type(movies)==int:
        pass
    else:
        print(movies)   


    
    
get_movie_name()