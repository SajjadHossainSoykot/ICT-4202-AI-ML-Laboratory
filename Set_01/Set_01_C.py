"""ICT-4202 AI & ML Laboratory — Set 01, Question 3.
Iris k-NN and standardization
Run: python Set_01/Set_01_C.py
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,
                                                    stratify=y, random_state=42)
print('Iris samples:', X.shape, '| train:', len(y_train), '| test:', len(y_test))
print('Class order:', list(iris.target_names))

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
results = []
models = {}
for k in [1,3,5,7]:
    m = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    pred = m.predict(X_test)
    results.append({'k':k, 'test_accuracy':accuracy_score(y_test,pred)})
    models[k] = m
table = pd.DataFrame(results)
print(table.to_string(index=False))
best_k = sorted(results, key=lambda d: (-d['test_accuracy'],d['k']))[0]['k']
best_pred = models[best_k].predict(X_test)
print(f'Best k on this fixed test split: {best_k}')
print('Confusion matrix (rows=true, columns=predicted):\n', confusion_matrix(y_test,best_pred))
scaled_knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=best_k))
scaled_knn.fit(X_train, y_train)
scaled_pred = scaled_knn.predict(X_test)
print('Unscaled accuracy:', round(accuracy_score(y_test,best_pred),4))
print('Scaled accuracy:', round(accuracy_score(y_test,scaled_pred),4))
print('Scaled confusion matrix:\n', confusion_matrix(y_test,scaled_pred))
ConfusionMatrixDisplay.from_predictions(y_test, best_pred, display_labels=iris.target_names,
                                        cmap='Blues', xticks_rotation=20)
plt.title(f'Iris k-NN (unscaled; k={best_k})'); plt.tight_layout(); plt.show()
