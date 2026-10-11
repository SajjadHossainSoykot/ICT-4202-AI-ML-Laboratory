"""ICT-4202 AI & ML Laboratory — Set 07, Question 3.
K-means with and without scaling
Run: python Set_07/Set_07_C.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
iris = load_iris()

X=iris.data.copy()
raw=KMeans(n_clusters=3,random_state=42,n_init=10).fit(X)
scaler=StandardScaler().fit(X)
X_scaled=scaler.transform(X)
scaled=KMeans(n_clusters=3,random_state=42,n_init=10).fit(X_scaled)
for name,features,fit in [('Original cm',X,raw),('Standardized z-scores',X_scaled,scaled)]:
    print(f'\n{name}: inertia={fit.inertia_:.4f}, silhouette={silhouette_score(features,fit.labels_):.4f}')
    print('Centroids in model coordinate system:\n',fit.cluster_centers_.round(3))
print('\nScaled centroids mapped BACK to cm (for interpretation; order is arbitrary):\n',
      scaler.inverse_transform(scaled.cluster_centers_).round(3))
for title,labels in [('Unscaled clustering',raw.labels_),('Scaled clustering',scaled.labels_)]:
    plt.figure(figsize=(7.5,4.8))
    plt.scatter(X[:,0],X[:,1],c=labels,cmap='viridis',alpha=.85,s=38)
    plt.xlabel('Sepal length (cm)');plt.ylabel('Sepal width (cm)')
    plt.title(title+' (showing only two of four fitted features)');plt.tight_layout();plt.show()
