"""ICT-4202 AI & ML Laboratory — Set 10, Question 2.
BFS, Greedy and A* comparison
Run: python Set_10/Set_10_B.py
"""

from collections import deque
import heapq

# Graph with positive edge costs
graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('C', 9), ('D', 8)],
    'B': [('D', 1), ('E', 4)],
    'C': [('G', 7)],
    'D': [('G', 2)],
    'E': [('G', 6)],
    'G': []
}

# Heuristic values
h = {'S': 4, 'A': 1, 'B': 3, 'C': 2, 'D': 1, 'E': 5, 'G': 0}

# Breadth-First Search
def bfs():
    q = deque([('S', ['S'])])
    seen = {'S'}
    trace = []

    while q:
        node, path = q.popleft()
        trace.append(node)

        if node == 'G':
            return path, trace

        for nxt, cost in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, path + [nxt]))

# Greedy Best-First Search
def greedy():
    q = [(h['S'], 0, 'S', ['S'])]
    seen = set()
    trace = []
    cost = 0

    while q:
        _, _, node, path = heapq.heappop(q)

        if node in seen:
            continue
        seen.add(node)
        trace.append(node)

        if node == 'G':
            return path, trace

        for nxt, w in graph[node]:
            if nxt not in seen:
                heapq.heappush(
                    q, (h[nxt], len(trace), nxt, path + [nxt])
                )

# A* Search
def astar():
    q = [(h['S'], 0, 'S', ['S'])]
    best = {'S': 0}
    trace = []

    while q:
        f, g, node, path = heapq.heappop(q)

        if g != best[node]:
            continue
        trace.append((node, g, h[node], f))

        if node == 'G':
            return path, g, trace

        for nxt, w in graph[node]:
            new_g = g + w
            if new_g < best.get(nxt, float('inf')):
                best[nxt] = new_g
                heapq.heappush(
                    q, (new_g + h[nxt], new_g, nxt, path + [nxt])
                )

# Calculate path cost
def cost(path):
    return sum(
        next(w for v, w in graph[u] if v == nxt)
        for u, nxt in zip(path, path[1:])
    )

# Run all algorithms
p1, t1 = bfs()
p2, t2 = greedy()
p3, c3, t3 = astar()

print("BFS:", p1, "| Trace:", t1, "| Cost:", cost(p1))
print("Greedy:", p2, "| Trace:", t2, "| Cost:", cost(p2))

print("A*:", p3, "| Cost:", c3)
print("A* Expansion Trace:")

print("Node     g(n)     h(n)     f(n)")
for n, g, hv, f in t3:
    print(f"{n:>4} {g:>8} {hv:>8} {f:>8}")
