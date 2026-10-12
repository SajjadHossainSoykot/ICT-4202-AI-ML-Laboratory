# ICT-4202 — Artificial Intelligence and Machine Learning Laboratory

**Department of Information and Communication Technology**  
**Islamic University, Kushtia, Bangladesh**  
**Course Code:** ICT-4202

This repository contains solutions and study notebooks for the **10 final laboratory examination question sets** of ICT-4202. Each set has a Jupyter notebook with explanations, mathematical equations, code, results, and viva notes, plus four separate Python files: A, B, and C for the three practical questions, and D for Q4 viva revision.

**GitHub repository:** [SajjadHossainSoykot/ICT-4202-AI-ML-Laboratory](https://github.com/SajjadHossainSoykot/ICT-4202-AI-ML-Laboratory)

## Laboratory question sets

| Set | Q1: A | Q2: B | Q3: C | Q4: Viva D | Complete notebook |
|:---:|:---|:---|:---|:---|:---|
| 01 | [Simple reflex vacuum and PEAS](Set_01/Set_01_A.py) | [BFS, DFS and Greedy Best-First](Set_01/Set_01_B.py) | [Iris k-NN and standardization](Set_01/Set_01_C.py) | [Viva practice](Set_01/Set_01_D.py) | [Open notebook](Set_01/Set_01_Solutions.ipynb) |
| 02 | [Forward chaining with weather facts](Set_02/Set_02_A.py) | [Depth-Limited Search and IDDFS](Set_02/Set_02_B.py) | [Simple linear regression](Set_02/Set_02_C.py) | [Viva practice](Set_02/Set_02_D.py) | [Open notebook](Set_02/Set_02_Solutions.ipynb) |
| 03 | [FOL family relationships](Set_03/Set_03_A.py) | [A* and uniform-cost search](Set_03/Set_03_B.py) | [Iris K-means model selection](Set_03/Set_03_C.py) | [Viva practice](Set_03/Set_03_D.py) | [Open notebook](Set_03/Set_03_Solutions.ipynb) |
| 04 | [BFS, DFS and bidirectional search](Set_04/Set_04_A.py) | [WEKA J48 and IBk (GUI task)](Set_04/Set_04_B.py) | [Linear regression and changed target](Set_04/Set_04_C.py) | [Viva practice](Set_04/Set_04_D.py) | [Open notebook](Set_04/Set_04_Solutions.ipynb) |
| 05 | [Three-room cleaning agent](Set_05/Set_05_A.py) | [Greedy versus A*](Set_05/Set_05_B.py) | [Decision-tree depth selection](Set_05/Set_05_C.py) | [Viva practice](Set_05/Set_05_D.py) | [Open notebook](Set_05/Set_05_Solutions.ipynb) |
| 06 | [Exam eligibility inference](Set_06/Set_06_A.py) | [BFS, DFS and IDDFS](Set_06/Set_06_B.py) | [k-NN versus decision tree](Set_06/Set_06_C.py) | [Viva practice](Set_06/Set_06_D.py) | [Open notebook](Set_06/Set_06_Solutions.ipynb) |
| 07 | [FOL relations and siblings](Set_07/Set_07_A.py) | [Greedy and misleading heuristic](Set_07/Set_07_B.py) | [K-means with and without scaling](Set_07/Set_07_C.py) | [Viva practice](Set_07/Set_07_D.py) | [Open notebook](Set_07/Set_07_Solutions.ipynb) |
| 08 | [DLS and IDDFS](Set_08/Set_08_A.py) | [WEKA preprocessing, IBk and J48 (GUI task)](Set_08/Set_08_B.py) | [Linear regression with a train/test split](Set_08/Set_08_C.py) | [Viva practice](Set_08/Set_08_D.py) | [Open notebook](Set_08/Set_08_Solutions.ipynb) |
| 09 | [BFS/DFS and adjacency ordering](Set_09/Set_09_A.py) | [A* heuristic admissibility](Set_09/Set_09_B.py) | [K-means inertia and silhouette](Set_09/Set_09_C.py) | [Viva practice](Set_09/Set_09_D.py) | [Open notebook](Set_09/Set_09_Solutions.ipynb) |
| 10 | [Integrated knowledge-based agent](Set_10/Set_10_A.py) | [BFS, Greedy and A* comparison](Set_10/Set_10_B.py) | [k-NN versus decision tree metrics](Set_10/Set_10_C.py) | [Viva practice](Set_10/Set_10_D.py) | [Open notebook](Set_10/Set_10_Solutions.ipynb) |

## Repository structure

```text
ICT-4202-AI-ML-Laboratory/
├── README.md
├── All_Sets_Solutions.ipynb       # Combined master notebook (Sets 01–10; PDF export ready)
├── requirements.txt
├── Set_01/
│   ├── Set_01_Solutions.ipynb
│   ├── Set_01_A.py
│   ├── Set_01_B.py
│   ├── Set_01_C.py
│   └── Set_01_D.py
├── Set_02/  ...
├── ...
└── Set_10/
    ├── Set_10_Solutions.ipynb
    ├── Set_10_A.py
    ├── Set_10_B.py
    ├── Set_10_C.py
    └── Set_10_D.py
```

## How to run

Install Python 3.10+ and the required packages:

```bash
python -m pip install -r requirements.txt
```

**Notebooks:**
- **Combined Master Notebook:** Open [`All_Sets_Solutions.ipynb`](All_Sets_Solutions.ipynb) in JupyterLab, VS Code, or Colab for the complete unified solutions across all 10 sets (pre-rendered figures and outputs, formatted for reading and direct PDF export).
- **Per-Set Notebooks:** Open any `Set_XX/Set_XX_Solutions.ipynb` to work with an individual set.

**Python script:** Run any practical question individually from the repository root:

```bash
python Set_01/Set_01_A.py
python Set_01/Set_01_B.py
python Set_01/Set_01_C.py
python Set_01/Set_01_D.py       # Q4 viva questions and answers
python Set_01/Set_01_D.py --quiz # Optional viva self-test
```

For other question sets, replace `01` with the relevant set number (`02`–`10`).

**Question mapping:** A = Q1, B = Q2, C = Q3, D = Q4 (Viva Voce, 10 marks). Q1-Q3 scripts include all requested subparts; Q4 is oral and the D script is optional study practice.

**WEKA:** Questions 4-B and 8-B require WEKA Explorer. The corresponding `.py` files verify `iris.arff`; the notebooks contain the WEKA GUI steps. Run J48 and IBk in WEKA itself, record your accuracy/confusion matrices, and save screenshots or result buffers.

## References

- *ICT-4202: Artificial Intelligence and Machine Learning Laboratory Manual*, Prof. Dr. Md. Zahidul Islam, Department of ICT, Islamic University.
- [AI_and_ML_Laboratory](https://github.com/sazidshahjada/AI_and_ML_Laboratory) — supplementary example code reference.
- [AI-ML](https://github.com/md-julfikar/AI-ML) — supplementary example code reference.

---

**Maintained by:** [@SajjadHossainSoykot](https://github.com/SajjadHossainSoykot)  
*For academic study and laboratory practice.*
