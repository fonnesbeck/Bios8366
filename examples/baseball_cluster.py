from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd

# Import data
baseball = pd.read_csv("../data/baseball.csv", index_col=0)

## Write answer h# Generate statistics
baseball = baseball[baseball.ab>100].copy()
hit_rate = baseball.h.astype(float) / baseball.ab
strikeout_rate = baseball.so.astype(float) / baseball.ab
walk_rate = baseball.bb.astype(float) / baseball.ab

# Create feature matrix
X = np.c_[hit_rate, strikeout_rate, walk_rate]

# Run PCA
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)

# Run clustering
km_baseball = KMeans(n_clusters=3).fit(X_pca)

baseball_clust = pd.DataFrame(X_pca, 
                              columns=['First Component', 'Second Component'])
baseball_clust['Cluster'] = km_baseball.labels_

sns.lmplot('First Component', 'Second Component', 
           data=baseball_clust, 
           fit_reg=False, 
           hue="Cluster")

baseball.player.values[km_baseball.labels_==2]