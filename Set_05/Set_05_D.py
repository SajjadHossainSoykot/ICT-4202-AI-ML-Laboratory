"""ICT-4202 AI/ML Laboratory - Set 05, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_05/Set_05_D.py
    python Set_05/Set_05_D.py --quiz
"""

import sys

QUESTIONS = [
    ('Simple reflex agent?', 'Uses condition-action rules based on current percept only.'),
    ('What is a state?', 'Current representation of the environment/problem.'),
    ('Greedy versus A*?', 'Greedy minimizes h; A* minimizes g+h.'),
    ('What is a tree split?', 'A feature-and-threshold test dividing samples.'),
    ('Underfitting?', 'Model too simple to learn relevant patterns.'),
    ('Overfitting?', 'Model fits training details/noise and generalizes poorly.'),
    ('Precision/Recall/F1?', 'Precision: TP/(TP+FP); recall: TP/(TP+FN); F1: harmonic mean.'),
    ('Why is Greedy not always optimal?', 'It considers h(n) only and can ignore the cost already paid, g(n).'),
    ('Why compare training and test accuracy?', 'A large training-test performance gap can indicate overfitting.'),
]


def review():
    print("SET 05 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 05 - VIVA PRACTICE")
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
