"""ICT-4202 AI & ML Laboratory — Set 10, Question 3.
k-NN versus decision tree metrics
Run: python Set_10/Set_10_C.py
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
from sklearn.metrics import precision_recall_fscore_support
candidates={'k-NN (k=3)':KNeighborsClassifier(n_neighbors=3),
            'Decision tree (depth=3)':DecisionTreeClassifier(max_depth=3,random_state=42)}
rows=[]
for name,model in candidates.items():
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    accuracy=accuracy_score(y_test,pred)
    p,r,f1,_=precision_recall_fscore_support(y_test,pred,average='macro',zero_division=0)
    rows.append({'model':name,'accuracy':accuracy,'precision_macro':p,
                 'recall_macro':r,'f1_macro':f1})
    errors=np.flatnonzero(pred!=y_test)
    print('\n'+name)
    print('Confusion matrix (actual rows):\n',confusion_matrix(y_test,pred))
    print('Misclassified TEST ROW POSITIONS:',errors.tolist())
    for idx in errors[:10]:
        print('  Row',idx,'| actual:',iris.target_names[y_test[idx]],
              '| predicted:',iris.target_names[pred[idx]])
comparison=pd.DataFrame(rows)
print(comparison.round(4).to_string(index=False))
winner=comparison.sort_values(['accuracy','f1_macro','model'],ascending=[False,False,True]).iloc[0]
print('Preferred for this particular split (accuracy then macro F1):',winner['model'])
