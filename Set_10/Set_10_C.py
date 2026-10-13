"""ICT-4202 AI & ML Laboratory — Set 10, Question 3.
k-NN versus decision tree metrics
Run: python Set_10/Set_10_C.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    precision_recall_fscore_support, ConfusionMatrixDisplay
)

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
names = iris.target_names

# Split: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)

print("Iris samples:", X.shape)
print("Training:", len(y_train), "| Testing:", len(y_test))
print("Class order:", list(names))

# Define models
models = [
    ("k-NN (k=3)", KNeighborsClassifier(n_neighbors=3)),
    ("Decision Tree (depth=3)",
     DecisionTreeClassifier(max_depth=3, random_state=42))
]

results = []
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Train and evaluate
for (name, model), ax in zip(models, axes):
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    p, r, f1, _ = precision_recall_fscore_support(
        y_test, pred, average="macro", zero_division=0
    )
    results.append((name, acc, p, r, f1))

    print("\n", name)
    print("Accuracy:", round(acc, 4))
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
    print("Macro Precision:", round(p, 4))
    print("Macro Recall:", round(r, 4))
    print("Macro F1-score:", round(f1, 4))
    print(classification_report(
        y_test, pred, target_names=names, zero_division=0
    ))

    wrong = np.where(pred != y_test)[0]
    print("Misclassified test rows:")
    for i in wrong:
        print(i, "| Actual:", names[y_test[i]],
              "| Predicted:", names[pred[i]])

    ConfusionMatrixDisplay.from_predictions(
        y_test, pred, display_labels=names,
        cmap="Blues", values_format="d",
        colorbar=False, ax=ax
    )
    ax.set_title(name)

# Display confusion matrices
plt.tight_layout()
plt.show()

# Compare models
print("\nModel Comparison")
print("{:<25} {:>10} {:>12} {:>10} {:>10}".format(
    "Model", "Accuracy", "Precision", "Recall", "F1-score"
))

for name, acc, p, r, f1 in results:
    print("{:<25} {:>10.4f} {:>12.4f} {:>10.4f} {:>10.4f}".format(
        name, acc, p, r, f1
    ))

# Select preferred model by accuracy, then F1-score
winner = max(results, key=lambda x: (x[1], x[4]))
print("\nPreferred model for this split:", winner[0])
