import clustering_code
import os
from matplotlib.pyplot import plot


def get_movie_name():
    input_movie=input("Enter a Movie Name: ")
    clean_t_dataset()
    movies=clustering_code.cluster_everything(input_movie)
    if type(movies)==int:
        pass
    else:
        print(movies)   

def clean_t_dataset():
    try:
        os.remove('ds_temp.csv')
    except:
        pass
    
    
get_movie_name()