"""ICT-4202 AI & ML Laboratory — Set 06, Question 3.
k-NN versus decision tree
Run: python Set_06/Set_06_C.py
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
from sklearn.tree import DecisionTreeClassifier
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train,y_train)
dt = DecisionTreeClassifier(max_depth=3,random_state=42).fit(X_train,y_train)
for name, model in [('k-NN (k=5)',knn),('Decision tree (depth=3)',dt)]:
    preds=model.predict(X_test)
    errors=np.flatnonzero(preds!=y_test)
    print(f'\n{name}: accuracy={accuracy_score(y_test,preds):.4f}')
    print('Confusion matrix (actual rows):\n',confusion_matrix(y_test,preds))
    print('Misclassified TEST ROW POSITIONS:',errors.tolist())
    for idx in errors[:10]:
        print(' ',idx, 'true:',iris.target_names[y_test[idx]],
              'predicted:',iris.target_names[preds[idx]],
              'features:',np.round(X_test[idx],2).tolist())
scaled_knn=make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=5))
scaled_knn.fit(X_train,y_train)
scaled_pred=scaled_knn.predict(X_test)
print('\nScaled k-NN accuracy:',round(accuracy_score(y_test,scaled_pred),4))
print('Scaled confusion matrix:\n',confusion_matrix(y_test,scaled_pred))
