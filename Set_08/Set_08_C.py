"""ICT-4202 AI & ML Laboratory — Set 08, Question 3.
Linear regression with a train/test split
Run: python Set_08/Set_08_C.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# Student practice dataset (synthetic): study hours -> exam score.
# Explicitly illustrative, NOT student survey/observed exam results.
hours=np.arange(1,17,dtype=float)
rng=np.random.default_rng(42)
scores=12+4.0*hours+rng.normal(0,2.5,size=hours.size)
X=hours.reshape(-1,1)
X_train,X_test,y_train,y_test=train_test_split(X,scores,test_size=.25,random_state=42)
model=LinearRegression().fit(X_train,y_train)
print('Samples:',len(hours),'| Train:',len(y_train),'| Test:',len(y_test))
print(f'Slope={model.coef_[0]:.4f}, intercept={model.intercept_:.4f}')
print(f'Train R²={r2_score(y_train,model.predict(X_train)):.4f}')
print(f'Test  R²={r2_score(y_test,model.predict(X_test)):.4f}')
for unseen in [7.5,18.0]:
    print(f'Prediction for {unseen} study hours: {model.predict([[unseen]])[0]:.3f}')
line=np.linspace(0.5,18.5,120).reshape(-1,1)
plt.figure(figsize=(8,4.8))
plt.scatter(X_train[:,0],y_train,label='Training data')
plt.scatter(X_test[:,0],y_test,marker='s',label='Test data')
plt.plot(line[:,0],model.predict(line),label='Fitted regression')
plt.xlabel('Hours studied');plt.ylabel('Exam score (synthetic)')
plt.title('Set 08: synthetic study-hours regression')
plt.grid(alpha=.2);plt.legend();plt.tight_layout();plt.show()
