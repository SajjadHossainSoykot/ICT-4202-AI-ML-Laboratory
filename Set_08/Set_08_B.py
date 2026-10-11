"""ICT-4202 AI & ML Laboratory — Set 08, Question 2.
WEKA preprocessing, IBk and J48 (GUI task)
Run: python Set_08/Set_08_B.py
"""

from scipy.io import arff
from pathlib import Path
from collections import Counter
# Use the same data file in a notebook and in a standalone Python script.
try:
    iris_path = Path(__file__).with_name("iris.arff")
except NameError:  # Jupyter notebooks do not define __file__.
    iris_path = Path("iris.arff")
records, meta=arff.loadarff(iris_path)
counts=Counter(x.decode('utf-8') for x in records['class'])
print('ARFF for WEKA:',iris_path.resolve())
print('Attributes:',meta.names())
print('Instances:',len(records),'| class distribution:',dict(counts))
assert len(records)==150
print("NOTE: These are dataset checks only; run J48/IBk in WEKA Explorer and record its real results.")
