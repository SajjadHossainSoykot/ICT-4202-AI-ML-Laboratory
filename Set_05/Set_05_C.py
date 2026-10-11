"""ICT-4202 AI & ML Laboratory — Set 05, Question 3.
Decision-tree depth selection
Run: python Set_05/Set_05_C.py
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

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
scores, trained={},{ }
for depth in [1,2,3,4,None]:
    model=DecisionTreeClassifier(max_depth=depth,random_state=42).fit(X_train,y_train)
    scores[depth]=(model.score(X_train,y_train),model.score(X_test,y_test))
    trained[depth]=model
results=pd.DataFrame([{'max_depth':str(d),'train_acc':scores[d][0],
                       'test_acc':scores[d][1]} for d in [1,2,3,4,None]])
print(results.round(4).to_string(index=False))
# Deterministic ties: prefer the simplest depth, with unlimited last.
best_depth=max([1,2,3,4,None],key=lambda d:(scores[d][1],-({None:999}.get(d,d))))
best=trained[best_depth]
pred=best.predict(X_test)
print('Best depth (on given holdout):',best_depth)
print('Confusion matrix:\n',confusion_matrix(y_test,pred))
print(classification_report(y_test,pred,target_names=iris.target_names,zero_division=0))
depth_names=['1','2','3','4','None']
plt.figure(figsize=(7.8,4.6))
plt.plot(depth_names,results.train_acc,marker='o',label='Train')
plt.plot(depth_names,results.test_acc,marker='s',label='Test')
plt.xlabel('Tree max_depth');plt.ylabel('Accuracy');plt.ylim(0.45,1.02)
plt.title('Iris tree depth versus generalization');plt.grid(alpha=.2);plt.legend();plt.tight_layout();plt.show()
ConfusionMatrixDisplay.from_predictions(y_test,pred,display_labels=iris.target_names,
                                        cmap='Blues',xticks_rotation=20)
plt.title(f'Best decision tree (max_depth={best_depth})');plt.tight_layout();plt.show()
