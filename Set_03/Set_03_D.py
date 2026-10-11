"""ICT-4202 AI/ML Laboratory - Set 03, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_03/Set_03_D.py
    python Set_03/Set_03_D.py --quiz
"""

import sys

QUESTIONS = [
    ('What is a predicate?', 'A relation/property symbol such as Parent(x,y).'),
    ('What is tuple matching?', 'Binding the same intermediate object across relation facts.'),
    ('What is g(n)?', 'Accumulated path cost from the start.'),
    ('What is h(n)?', 'Estimated remaining goal cost.'),
    ('What is f(n)?', 'A* priority: g(n)+h(n).'),
    ('What is a centroid?', 'Mean feature vector of a cluster.'),
    ('What is inertia?', 'Sum of squared distances to assigned centroids.'),
    ('What is silhouette?', 'Cluster cohesion-versus-separation score.'),
    ('What is a constant in first-order logic?', 'A symbol naming a specific object, such as Ali or Rina.'),
    ('What is a variable in first-order logic?', 'A placeholder, such as x or y, that may refer to different objects.'),
    ('What does admissible mean for h(n)?', 'The estimate never exceeds the actual least remaining cost to the goal.'),
]


def review():
    print("SET 03 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 03 - VIVA PRACTICE")
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
