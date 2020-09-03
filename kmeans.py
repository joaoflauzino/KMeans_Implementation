
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import argparse
import pandas as pd

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-inputFile',
        default='iris.csv',
        type=str,
        help='name of file that will be worked')
    parser.add_argument(
        '-sep',
        default=',',
        help='column identifier')
    parser.add_argument(
        '-dec',
        default='.',
        help='decimal identifier')
    
    parser.add_argument(
        '-outputFile',
        default='results.csv',
        type=str,
        help='name of result file')

    parser.add_argument(
        '-K',
        default=5,
        type=int,
        help='groups number')

    parser.add_argument(
        '-n_iter',
        default=100,
        type=int,
        help='groups number')

    return parser.parse_args()

#Random centroids 
def init_clusters_random_centroids(X, m, n, K):
    centroids=np.array([]).reshape(n,0) 
    for i in range(K):
        rand=rd.randint(0,m-1)
        centroids=np.c_[centroids,X[rand]]

    return centroids

#Calculate distances
def calculate_distance_Euclidean(Centroids, m, K, X):
    distance = np.array([]).reshape(m,0)
    for k in range(K):
        dist = np.sum((X-Centroids[:,k])**2,axis=1)
        distance = np.c_[distance, dist]

    return np.argmin(distance, axis=1)+1

def write_file(df, outputFile):
    return df.to_csv('output/' + outputFile)

def generate_scatter(df, group):
    import seaborn as sns
    datasets = {"original": df.select_dtypes(exclude=['object']), "predict": group}
    for k, v in datasets.items():
        if k == 'original':
            sns.lmplot(x=v.columns[0], y=v.columns[1], data=v, fit_reg=False, legend=False)
        else:
            sns.lmplot(x=v.columns[0], y=v.columns[1], data=v, hue="predict", fit_reg=False, legend=False)
        plt.savefig('output/' + k + '.png')

#Grouping data
def main(n_iter, K, df, outputFile):

    columns = df.select_dtypes(exclude=['object']).columns.tolist()
    columns.append('predict')
    X = df.select_dtypes(exclude=['object']).values
    m=X.shape[0] #training examples
    n=X.shape[1] #number of features
   
    centroids = init_clusters_random_centroids(X, m, n, K)

    for i in range(n_iter):
        min_distance = calculate_distance_Euclidean(centroids, m, K, X)
        results = {}
        for k in range(K):
            results[k+1] = np.array([]).reshape(n,0)
        for i in range(m):
            results[min_distance[i]] = np.c_[results[min_distance[i]], X[i]]
        for k in range(K):
            results[k+1] = results[k+1].T
        for k in range(K):
            centroids[:,k] = np.mean(results[k+1], axis = 0)


    group = pd.DataFrame(np.asarray([np.append(j, i) for i in list(results.keys()) for j in results[i]]), columns = columns)
    generate_scatter(df, group) # Generate scatter plots
    write_file(group, outputFile) # write file

    return group

if __name__ == "__main__":
    
    args = get_args()
    df = pd.read_csv('dataset/' + args.inputFile, sep=args.sep, decimal=args.dec)
    main(args.n_iter, args.K, df, args.outputFile)

   