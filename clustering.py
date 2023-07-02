import preprocessing
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import random


def Clustered_final_df(df):
    df['Cluster_Id'] = None
    
    kmeans = KMeans(n_clusters=75)
    
    features = df[['P_Genre','S_Genre','T_Genre']]
    label=kmeans.fit_predict(features)
    
    df['Cluster_Id']= label
    return df

def plot_clusters():
    points = pd.read_csv('ds_temp.csv')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = points['P_Genre'].values
    y = points['S_Genre'].values
    z = points['T_Genre'].values
    clust_id = points['Cluster_Id'].values
    
    number_of_colors = 75

    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(8)])
                for i in range(number_of_colors)]

    
    for i in range(x.size):
        ax.scatter(x[i], y[i], z[i],color=colors[clust_id[i]%6], marker='o')

    plt.show()

def cluster_everything(input_movie):
    df = preprocessing.pre_process_all()

    df = Clustered_final_df(df)
    df.to_csv('ds_temp.csv')
    plot_clusters()
    input_movie = input_movie.lower()
    try:
        movie_not_found = df.loc[~df['Movie'].str.contains(input_movie)]
        if len(movie_not_found) == 0:
            print('Movie not found')
            return 0
        get_cluster = df['Cluster_Id'].loc[df['Movie'].str.contains(input_movie)].values[0]
        similar_movies_list = df['Movie'].loc[df['Cluster_Id'] == get_cluster].values
        return similar_movies_list
    except:
        print('Movie not found')
        return 0


test = cluster_everything('men')
# for item in test:
#     print(item)

