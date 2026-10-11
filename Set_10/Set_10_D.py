"""ICT-4202 AI/ML Laboratory - Set 10, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_10/Set_10_D.py
    python Set_10/Set_10_D.py --quiz
"""

import sys

QUESTIONS = [
    ('What is an asserted fact?', 'A proposition initially placed into the KB.'),
    ('What is an inferred fact?', 'A new proposition derived using rules.'),
    ('Difference between BFS and A*?', 'BFS minimizes edge count; A* uses costs g+h.'),
    ('Greedy drawback?', 'It may favor a low h while ignoring high path cost g.'),
    ('Confusion matrix?', 'Counts of actual versus predicted classes.'),
    ('Precision?', 'Share of predicted positives that are truly positive.'),
    ('Recall?', 'Share of actual positives correctly predicted.'),
    ('F1?', 'Harmonic mean of precision and recall.'),
    ('What is forward chaining?', 'Start with known facts and repeatedly apply rules whose premises are satisfied.'),
    ('Does a shortest path in edges always have the lowest cost?', 'No. When edges have different costs, a path with fewer edges can cost more.'),
    ('What is the F1 score?', 'The harmonic mean of precision and recall: F1 = 2PR/(P+R), when P+R is positive.'),
]


def review():
    print("SET 10 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 10 - VIVA PRACTICE")
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
