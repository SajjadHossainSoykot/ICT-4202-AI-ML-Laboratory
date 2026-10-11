"""ICT-4202 AI/ML Laboratory - Set 08, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_08/Set_08_D.py
    python Set_08/Set_08_D.py --quiz
"""

import sys

QUESTIONS = [
    ('Depth cutoff?', 'A search boundary that may hide deeper goals.'),
    ('Why IDDFS repeats root?', 'Because each larger depth limit starts a new DFS.'),
    ('Cross-validation?', 'Repeated train/evaluate cycles on different held-out folds.'),
    ('What is data leakage?', 'Using test/validation information while training or preprocessing.'),
    ('What is standardization?', 'Subtract training mean and divide by training standard deviation.'),
    ('Train versus test R²?', 'In-sample fit versus fit on held-out observations.'),
    ('What is extrapolation?', 'Predicting beyond the range of available training inputs.'),
    ('What is the difference between normalization and standardization?', 'Min-max normalization usually rescales to a range such as 0 to 1; standardization subtracts the mean and divides by standard deviation.'),
    ('Why should preprocessing be fit within each training fold?', 'Fitting preprocessing on all data can leak information into cross-validation estimates.'),
]


def review():
    print("SET 08 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 08 - VIVA PRACTICE")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        try:
            input("Think of your answer, then press Enter to reveal it...")
        except EOFError:
            pass
        print(f"Answer: {answer}")


if __name__ == "__main__":
    if "--quiz" in sys.argv[1:]:
        quiz()
    else:
        review()
