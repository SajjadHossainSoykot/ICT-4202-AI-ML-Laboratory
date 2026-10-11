"""ICT-4202 AI/ML Laboratory - Set 07, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_07/Set_07_D.py
    python Set_07/Set_07_D.py --quiz
"""

import sys

QUESTIONS = [
    ('What is FOL?', 'Logic with objects, predicates, variables, and quantifiers.'),
    ('What makes two people siblings?', 'They share a parent and are distinct people.'),
    ('What is Greedy best-first?', 'Heuristic-priority search using h only.'),
    ('Can misleading heuristics add expansions?', 'Yes; they may prioritize a branch that does not advance toward the goal.'),
    ('Is K-means supervised?', 'No; it does not use class labels during fit.'),
    ('What does scaling affect?', 'The distances, and thus centroids, cluster assignments, and inertia.'),
    ('What is silhouette?', 'A dimensionless separation/cohesion measure within one feature space.'),
    ('What is a binary relation?', 'A predicate connecting two objects, such as Parent(Rahman, Hasan).'),
    ('Why not compare K-means inertia before and after scaling directly?', 'Scaling changes the numerical distances and therefore changes the units and magnitude of inertia.'),
]


def review():
    print("SET 07 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 07 - VIVA PRACTICE")
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
