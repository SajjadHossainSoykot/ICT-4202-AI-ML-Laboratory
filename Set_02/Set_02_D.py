"""ICT-4202 AI/ML Laboratory - Set 02, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_02/Set_02_D.py
    python Set_02/Set_02_D.py --quiz
"""

import sys

QUESTIONS = [
    ('What is forward chaining?', 'Repeated application of satisfied rules to asserted facts.'),
    ('What is a knowledge base?', 'A set of encoded facts and rules.'),
    ('What is cutoff?', 'Search reaches the specified limit before ruling out deeper goals.'),
    ('Why IDDFS revisits the root?', 'It restarts DLS with an incremented limit.'),
    ('What is regression slope?', 'Expected change in predicted response for a one-unit predictor change.'),
    ('What is the intercept?', 'Predicted response at input zero.'),
    ('What does R² measure?', 'Goodness of fit relative to predicting the response mean.'),
    ('How is a fact different from a rule?', 'A fact is currently known, such as Cloudy. A rule is an implication such as Cloudy implies Rain.'),
    ('What is depth-limited search (DLS)?', 'A depth-first search that does not expand any node beyond a specified depth limit.'),
    ('What is IDDFS?', 'Iterative Deepening Depth-First Search runs DLS at increasing limits until a goal is found.'),
]


def review():
    print("SET 02 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 02 - VIVA PRACTICE")
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
