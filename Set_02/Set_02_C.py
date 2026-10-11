"""ICT-4202 AI & ML Laboratory — Set 02, Question 3.
Simple linear regression
Run: python Set_02/Set_02_C.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X = np.array([1,2,3,4,5,6],dtype=float).reshape(-1,1)
y = np.array([4,5,8,9,11,14],dtype=float)
model = LinearRegression().fit(X,y)
y_changed = y.copy(); y_changed[-1] = 18
changed_model = LinearRegression().fit(X,y_changed)
for label, mdl, target in [('Original',model,y),('Modified last score',changed_model,y_changed)]:
    print(f'{label}: slope={mdl.coef_[0]:.4f}; intercept={mdl.intercept_:.4f}; '
          f'pred(7)={mdl.predict([[7]])[0]:.4f}; train R²={mdl.score(X,target):.4f}')
grid = np.linspace(1,7,80).reshape(-1,1)
plt.figure(figsize=(8,4.7))
plt.scatter(X[:,0],y,label='Original observations')
plt.scatter([6],[18],marker='x',s=95,label='Changed observation (6,18)')
plt.plot(grid[:,0],model.predict(grid),label='Original fitted line')
plt.plot(grid[:,0],changed_model.predict(grid),'--',label='Refitted line')
plt.xlabel('Study hours'); plt.ylabel('Score'); plt.title('Regression sensitivity to one target value')
plt.grid(alpha=0.2); plt.legend(); plt.tight_layout(); plt.show()
