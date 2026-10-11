"""ICT-4202 AI/ML Laboratory - Set 06, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_06/Set_06_D.py
    python Set_06/Set_06_D.py --quiz
"""

import sys

QUESTIONS = [
    ('Forward chaining?', 'Infer consequences repeatedly from satisfied premises.'),
    ('When is P→Q false?', 'When P is true but Q is false.'),
    ('What is a BFS frontier?', 'Queue of discovered paths/nodes awaiting expansion.'),
    ('Why IDDFS uses less memory than BFS?', 'It performs depth-limited DFS rather than storing a full breadth frontier.'),
    ('How k-NN works?', 'Votes among the k closest training instances.'),
    ('Why standardize k-NN inputs?', 'To reduce unit-driven dominance in distances.'),
    ('Decision tree?', 'Predicts via learned nested feature thresholds.'),
    ('Which data structure does DFS use?', 'A LIFO stack, or the program call stack in recursive DFS.'),
    ('How does IDDFS combine BFS and DFS benefits?', 'It finds a shallow goal by trying larger limits while retaining depth-first memory use.'),
]


def review():
    print("SET 06 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 06 - VIVA PRACTICE")
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
