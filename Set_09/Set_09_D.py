"""ICT-4202 AI/ML Laboratory - Set 09, Question 4: Viva Voce (10 marks).

Q4 is an ORAL examination question, not a programming task.
This standalone Python file is a quick-revision and self-quiz aid.

Commands:
    python Set_09/Set_09_D.py
    python Set_09/Set_09_D.py --quiz
"""

import sys

QUESTIONS = [
    ('Why BFS returns a shortest path?', 'FIFO exploration of increasing depth in an unweighted graph.'),
    ('Can DFS give a longer path?', 'Yes; DFS does not prioritize depth globally.'),
    ('Admissible heuristic?', 'h never overestimates the true remaining cheapest cost.'),
    ('A* priority?', 'f(n)=g(n)+h(n).'),
    ('What is inertia?', 'Sum of within-cluster squared deviations.'),
    ('What is an elbow?', 'A point where inertia improvement slows markedly.'),
    ('What does silhouette measure?', 'Similarity within the assigned cluster versus nearest other cluster.'),
    ('What happens if a heuristic overestimates the cost?', 'A* may lose its shortest-cost guarantee because the heuristic is not admissible.'),
    ('Why does K-means inertia usually decrease as k increases?', 'More centers can reduce or preserve the sum of distances to the nearest assigned center.'),
]


def review():
    print("SET 09 - Q4: VIVA VOCE (10 MARKS)")
    print("Oral exam preparation - no programming task is required for Q4.")
    for index, (question, answer) in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {question}")
        print(f"   Answer: {answer}")


def quiz():
    print("SET 09 - VIVA PRACTICE")
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
