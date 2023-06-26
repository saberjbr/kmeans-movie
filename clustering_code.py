import pre_processing
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt



def Clustered_final_df(df):
    df['Cluster_Id'] = None
    
    kmeans = KMeans(n_clusters=100)
    
    features = df[['P_Genre','S_Genre','T_Genre']]
    kmeans.fit(features)
    df['Cluster_Id'] = kmeans.predict(features)
    return df

def cluster_everything(input_movie):
    df = pre_processing.pre_process_all()

    df = Clustered_final_df(df)
    df.to_csv('ds_temp.csv')
    
 

    # plot
    plt_label = ['P_Genre','S_Genre','T_Genre']
    # plt_u_labels = np.unique(plt_label)
    # print('plt_u_labels: ',plt_u_labels)
    #for i in plt_label:
    plt.scatter(df[0] , df[1] ,df[2])
    plt.legend()
    plt.show()
    # end plot


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
for item in test:
    print(item)

