"""ICT-4202 AI & ML Laboratory — Set 09, Question 1.
BFS/DFS and adjacency ordering
Run: python Set_09/Set_09_A.py
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

def dfs(graph, start, goal):
    stack = [(start, [start])]
    seen = set()
    expanded = []
    while stack:
        node, path = stack.pop()
        if node in seen: continue
        seen.add(node)
        expanded.append(node)
        if node == goal:
            return path, expanded
        # Reverse push order so the FIRST listed neighbor is explored first.
        for nxt in reversed(graph.get(node, [])):
            if nxt not in seen:
                stack.append((nxt, path + [nxt]))
    return None, expanded

graph={'A':['B','C'],'B':['D','E'],'C':['F'],'D':['H'],
       'E':['G'],'F':['G'],'G':[],'H':['G']}
reversed_graph={u:list(reversed(v)) for u,v in graph.items()}
for name, variant in [('Original adjacency',graph),('Reversed adjacency',reversed_graph)]:
    print('\n'+name)
    for algorithm,fn in [('BFS',bfs),('DFS',dfs)]:
        path,expanded=fn(variant,'A','G')
        print(f'  {algorithm}: path={path}; edges={len(path)-1 if path else None}; expanded={expanded}')
