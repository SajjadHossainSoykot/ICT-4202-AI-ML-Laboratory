"""ICT-4202 AI & ML Laboratory — Set 03, Question 3.
Iris K-means model selection
Run: python Set_03/Set_03_C.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
iris = load_iris()

X = iris.data[:, :2]  # sepal length and sepal width (cm)
rows, cluster_models = [], {}
for k in [2,3,4,5]:
    model = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    score = silhouette_score(X,model.labels_)
    rows.append({'k':k,'inertia':model.inertia_,'silhouette':score})
    cluster_models[k]=model
table=pd.DataFrame(rows)
print(table.round(4).to_string(index=False))
selected_k=int(table.loc[table['silhouette'].idxmax(),'k'])
best=cluster_models[selected_k]
print('Selected k (highest silhouette among tested values):',selected_k)
print('Centroids (sepal length, sepal width):\n',best.cluster_centers_.round(3))
plt.figure(figsize=(8,5))
plt.scatter(X[:,0],X[:,1],c=best.labels_,alpha=.8,s=38,cmap='viridis')
plt.scatter(best.cluster_centers_[:,0],best.cluster_centers_[:,1],
            marker='X',s=220,c='red',edgecolors='black',label='Centroids')
plt.xlabel('Sepal length (cm)'); plt.ylabel('Sepal width (cm)')
plt.title(f'Iris clustering in first two features (k={selected_k})')
plt.legend(); plt.tight_layout(); plt.show()
