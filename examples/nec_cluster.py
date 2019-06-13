import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from itertools import cycle

def plot_2D(data, target, target_names, pca):
    colors = cycle('rgbcmykw')
    target_ids = range(len(target_names))
    plt.figure()
    for i, c, label in zip(target_ids, colors, target_names):
        plt.scatter(data[target == i, 0], data[target == i, 1],
                   c=c, label=label)
    var_explained = pca.explained_variance_ratio_ * 100
    plt.xlabel('First Component: {0:.1f}%'.format(var_explained[0]))
    plt.ylabel('Second Component: {0:.1f}%'.format(var_explained[1]))
    plt.legend()
    

microbiome = pd.read_csv("../data/microbiome.csv")

# Tissue samples
microbiome_pivoted = microbiome.pivot_table(index=['Patient', 'Group'], 
                        columns='Taxon')
tissue_data = microbiome_pivoted['Tissue']

tissue_pca = PCA(n_components=2, whiten=True).fit(tissue_data)
X_tissue_pca = tissue_pca.transform(tissue_data)

y_tissue = tissue_data.index.labels[1]

plot_2D(X_tissue_pca, y_tissue, ['Healthy', 'NEC'], tissue_pca)

km_tissue = KMeans(n_clusters=2)
km_tissue.fit(X_tissue_pca)

plot_2D(X_tissue_pca, km_tissue.labels_, ["c1", "c2"], tissue_pca)

# Stool samples
stool_data = microbiome_pivoted['Stool']

stool_pca = PCA(n_components=2, whiten=True).fit(stool_data)
X_stool_pca = stool_pca.transform(stool_data)

y_stool = stool_data.index.labels[1]

plot_2D(X_stool_pca, y_stool, ['Healthy', 'NEC'], stool_pca)