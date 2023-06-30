import pre_processing
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
import random


def Clustered_final_df(df):
    df['Cluster_Id'] = None
    
    kmeans = KMeans(n_clusters=100)
    
    features = df[['P_Genre','S_Genre','T_Genre']]
    label=kmeans.fit_predict(features)
    df['Cluster_Id']= label
  
    #plot
    # cols=df.columns
    # print('cols: ',cols)
    # label_0 = df[label == 0]
    # label_1 = df[label == 1]
    # label_2 = df[label == 2]
    # col_no=0
    # for i in df.columns:
    #     r = random.randint(0,255)
    #     g = random.randint(0,255)
    #     b = random.randint(0,255)
    #     rgb = [r,g,b]
    #     lbl=df[label==col_no]
    #     plt.scatter(lbl[cols[0]],lbl[cols[col_no]],color='green')
    #     col_no+=1

    # plt.scatter(label_0[cols[0]] , label_0[cols[1]], color = 'red')
    # plt.scatter(label_1[cols[0]] , label_1[cols[1]], color = 'black')
    # plt.scatter(label_2[cols[0]] , label_2[cols[1]], color = 'green')
    
    #plt.show()
    
#     from sklearn.datasets import make_swiss_roll
#     from mpl_toolkits.mplot3d import Axes3D
#    # X, t = make_swiss_roll(n_samples=1000, noise=0.2, random_state=42)
    

#     kmeans = KMeans(n_clusters=3)                   # Number of clusters == 3
#     kmeans = kmeans.fit(features)                          # Fitting the input data
#     labels = kmeans.predict(features)                      # Getting the cluster labels
#     centroids = kmeans.cluster_centers_             # Centroid values
#     # print("Centroids are:", centroids)              # From sci-kit learn


#     fig = plt.figure(figsize=(100,100))
#     ax = fig.add_subplot(projection='3d')
    

#     x = np.array(labels==3)
#     y = np.array(labels==4)
#     z = np.array(labels==5)


#     ax.scatter(centroids[:,0],centroids[:,1],centroids[:,2],c="black",s=150,label="Centers",alpha=1)
#     ax.scatter(features[x,0],features[x,1],features[x,2],c="blue",s=40,label="C1")
#     ax.scatter(features[y,0],features[y,1],features[y,2],c="yellow",s=40,label="C2")
#     ax.scatter(features[z,0],features[z,1],features[z,2],c="red",s=40,label="C3")

    return df

def cluster_everything(input_movie):
    df = pre_processing.pre_process_all()

    df = Clustered_final_df(df)
    df.to_csv('ds_temp.csv')
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

