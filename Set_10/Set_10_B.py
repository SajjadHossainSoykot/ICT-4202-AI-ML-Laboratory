"""ICT-4202 AI & ML Laboratory — Set 10, Question 2.
BFS, Greedy and A* comparison
Run: python Set_10/Set_10_B.py
"""

from collections import deque

import heapq

from itertools import count

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    seen = {start}
    expanded = []
    while queue:
        node, path = queue.popleft()
        expanded.append(node)
        if node == goal:
            return path, expanded
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None, expanded

from itertools import count

import heapq

def astar(graph, h, start, goal):
    counter = count()
    heap = [(h[start], next(counter), 0, start, [start])]
    best_g = {start: 0}
    expanded = []
    while heap:
        f, _, g, node, path = heapq.heappop(heap)
        if g > best_g.get(node, float('inf')): continue  # stale entry
        expanded.append((node, g, h[node], f))
        if node == goal: return path, g, expanded
        for nxt, weight in graph.get(node, []):
            new_g = g + weight
            if new_g < best_g.get(nxt, float('inf')):
                best_g[nxt] = new_g
                heapq.heappush(heap, (new_g+h[nxt], next(counter), new_g, nxt, path+[nxt]))
    return None, float('inf'), expanded

def greedy_weighted(graph, h, start, goal):
    counter = count()
    heap = [(h[start], next(counter), 0, start, [start])]
    seen, expanded = set(), []
    while heap:
        _, _, g, node, path = heapq.heappop(heap)
        if node in seen: continue
        seen.add(node)
        expanded.append((node, g, h[node]))
        if node == goal: return path, g, expanded
        for nxt, weight in graph.get(node, []):
            if nxt not in seen:
                heapq.heappush(heap, (h[nxt], next(counter), g+weight, nxt, path+[nxt]))
    return None, float('inf'), expanded

def display_astar_trace(trace):
    print("Node     g(n)     h(n)     f(n)")
    for node, g, h, f in trace:
        print(f"{node:>4} {g:>8} {h:>8} {f:>8}")

# Positive weights and an admissible (but deliberately uneven) heuristic are
# our EXPLICIT CHOICES: the examination question does not specify numbers.
weighted={'S':[('A',1),('B',2)],'A':[('C',9),('D',8)],
          'B':[('D',1),('E',4)],'C':[('G',7)],'D':[('G',2)],
          'E':[('G',6)],'G':[]}
unweighted={u:[v for v,c in edges] for u,edges in weighted.items()}
h={'S':4,'A':1,'B':3,'C':2,'D':1,'E':5,'G':0}
edge_cost={(u,v):cost for u,edges in weighted.items() for v,cost in edges}
def path_cost(path):
    return sum(edge_cost[(u,v)] for u,v in zip(path,path[1:])) if path else None
bfs_path,bfs_trace=bfs(unweighted,'S','G')
greedy_path,greedy_cost,greedy_trace=greedy_weighted(weighted,h,'S','G')
a_path,a_cost,a_trace=astar(weighted,h,'S','G')
print('BFS    :',bfs_path,'| expanded:',bfs_trace,'| cost:',path_cost(bfs_path))
print('Greedy :',greedy_path,'| expanded:',greedy_trace,'| cost:',greedy_cost)
print('A*     :',a_path,'| expanded:',a_trace,'| cost:',a_cost)
display_astar_trace(a_trace)
assert a_cost == 5 and path_cost(bfs_path) > a_cost
