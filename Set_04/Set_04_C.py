"""ICT-4202 AI & ML Laboratory — Set 04, Question 3.
Linear regression and changed target
Run: python Set_04/Set_04_C.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X=np.array([2,4,6,8,10,12],dtype=float).reshape(-1,1)
y=np.array([5,9,13,17,21,25],dtype=float)
fit=LinearRegression().fit(X,y)
print(f'Original: slope={fit.coef_[0]:.4f}; intercept={fit.intercept_:.4f}; '
      f'prediction(15)={fit.predict([[15]])[0]:.4f}; R²={fit.score(X,y):.4f}')
y_mod=y.copy(); y_mod[-1]=30  # Illustrative modification (question leaves value unspecified).
fit_mod=LinearRegression().fit(X,y_mod)
print(f'Changed last y (25→30): slope={fit_mod.coef_[0]:.4f}; '
      f'intercept={fit_mod.intercept_:.4f}; R²={fit_mod.score(X,y_mod):.4f}')
grid=np.linspace(2,15,80).reshape(-1,1)
plt.figure(figsize=(8,5))
plt.scatter(X[:,0],y,label='Original observations');plt.scatter([12],[30],marker='x',s=100,label='Changed y')
plt.plot(grid[:,0],fit.predict(grid),label='Original fit')
plt.plot(grid[:,0],fit_mod.predict(grid),'--',label='Modified fit')
plt.xlabel('Input X');plt.ylabel('Target Y');plt.title('Set 04: original vs modified regression')
plt.grid(alpha=.2);plt.legend();plt.tight_layout();plt.show()
