from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd

# Import data
baseball = pd.read_csv("../data/baseball.csv", index_col=0)

# Generate statistics
baseball = baseball[baseball.ab>100]
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

baseball.player.values[km_baseball.labels_==1]