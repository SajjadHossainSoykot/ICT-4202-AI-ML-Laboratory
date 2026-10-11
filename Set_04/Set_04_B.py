"""ICT-4202 AI & ML Laboratory — Set 04, Question 2.
WEKA J48 and IBk (GUI task)
Run: python Set_04/Set_04_B.py
"""

from pathlib import Path
from scipy.io import arff
from collections import Counter
# Use the same data file in a notebook and in a standalone Python script.
try:
    iris_path = Path(__file__).with_name("iris.arff")
except NameError:  # Jupyter notebooks do not define __file__.
    iris_path = Path("iris.arff")
data,meta=arff.loadarff(iris_path)
classes=[s.decode('utf-8') for s in data['class']]
print('File:',iris_path.resolve())
print('WEKA attributes:',meta.names())
print('Instances:',len(data),'| class counts:',dict(Counter(classes)))
assert len(data)==150 and len(set(classes))==3
print("NOTE: These are dataset checks only; run J48/IBk in WEKA Explorer and record its real results.")
