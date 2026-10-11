"""ICT-4202 AI/ML Laboratory - Set 04, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_04/Set_04_D.py
    python Set_04/Set_04_D.py --quiz
"""

import sys

QUESTIONS = [
    ('BFS versus DFS?', 'BFS expands breadth first (minimum-edge path); DFS follows a deep branch first.'),
    ('How to run backward search on directed edges?', 'Use the reverse adjacency graph.'),
    ('What is 10-fold CV?', 'Ten held-out validations, each using nine folds for training.'),
    ('What is J48?', 'WEKA decision tree learner based on C4.5.'),
    ('What is IBk?', 'WEKA nearest-neighbor classifier.'),
    ('What does a regression slope mean?', 'Predicted response change for one unit of input.'),
    ('What is bidirectional search?', 'Search from both start and goal, looking for a meeting point between the two frontiers.'),
    ('Why report expanded nodes?', 'Expanded-node counts let us compare the effort used by different search strategies.'),
]


def review():
    print("SET 04 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 04 - VIVA PRACTICE")
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
