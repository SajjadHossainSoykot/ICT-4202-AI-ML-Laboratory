"""ICT-4202 AI & ML Laboratory — Set 09, Question 3.
K-means inertia and silhouette
Run: python Set_09/Set_09_C.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
iris = load_iris()

X=iris.data[:, :2]
runs=[]; models={}
for k in [2,3,4,5]:
    mdl=KMeans(n_clusters=k,random_state=42,n_init=10).fit(X)
    models[k]=mdl
    runs.append({'k':k,'inertia':mdl.inertia_,'silhouette':silhouette_score(X,mdl.labels_)})
table=pd.DataFrame(runs)
print(table.round(4).to_string(index=False))
chosen_k=int(table.loc[table.silhouette.idxmax(),'k'])
best=models[chosen_k]
plt.figure(figsize=(7,4.4))
plt.plot(table.k,table.inertia,marker='o');plt.xticks([2,3,4,5]);plt.xlabel('Number of clusters k')
plt.ylabel('Inertia (within-cluster SSE)');plt.title('Elbow plot — first two Iris features')
plt.grid(alpha=.2);plt.tight_layout();plt.show()
plt.figure(figsize=(7,4.4))
plt.plot(table.k,table.silhouette,marker='s');plt.xticks([2,3,4,5]);plt.xlabel('k')
plt.ylabel('Silhouette score');plt.title('Cluster separation versus k')
plt.grid(alpha=.2);plt.tight_layout();plt.show()
print('Chosen by maximum silhouette:',chosen_k)
print('Centers:\n',best.cluster_centers_.round(3))
plt.figure(figsize=(7.6,5))
plt.scatter(X[:,0],X[:,1],c=best.labels_,cmap='viridis',s=35)
plt.scatter(best.cluster_centers_[:,0],best.cluster_centers_[:,1],marker='X',s=220,
            edgecolors='black',c='red',label='Centers')
plt.xlabel('Sepal length');plt.ylabel('Sepal width');plt.title(f'Final k-means (k={chosen_k})')
plt.legend();plt.tight_layout();plt.show()
