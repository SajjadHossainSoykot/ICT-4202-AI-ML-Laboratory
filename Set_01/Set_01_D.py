"""ICT-4202 AI/ML Laboratory - Set 01, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_01/Set_01_D.py
    python Set_01/Set_01_D.py --quiz
"""

import sys

QUESTIONS = [
    ('What is an intelligent agent?', 'A system that perceives its environment and selects actions.'),
    ('What does PEAS stand for?', 'Performance, Environment, Actuators, Sensors.'),
    ('Why BFS uses a queue?', 'FIFO yields shallowest-first expansion in an unweighted graph.'),
    ('How does Greedy select the next node?', 'It chooses minimum heuristic h(n).'),
    ('What is k in k-NN?', 'Number of nearest training samples considered.'),
    ('Why scale features?', 'So large-unit features do not automatically dominate distance.'),
    ('What is a confusion matrix?', 'Counts of true versus predicted classes.'),
    ('What is the main difference between BFS and DFS?', 'BFS uses a FIFO queue and explores level by level; DFS uses a stack or recursion and goes deep first.'),
    ('What is a heuristic function?', 'h(n) estimates the remaining cost or distance from node n to the goal.'),
    ('Give one PEAS example for a university delivery robot.', 'Performance: timely safe delivery; Environment: campus halls; Actuators: wheels and gripper; Sensors: camera and proximity sensor.'),
]


def review():
    print("SET 01 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 01 - VIVA PRACTICE")
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
