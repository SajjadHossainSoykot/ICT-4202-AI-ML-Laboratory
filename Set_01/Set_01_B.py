"""ICT-4202 AI & ML Laboratory — Set 01, Question 2.
BFS, DFS and Greedy Best-First
Run: python Set_01/Set_01_B.py
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

def greedy_unweighted(graph, h, start, goal):
    tie = count()
    heap = [(h[start], next(tie), start, [start])]
    seen, expanded = set(), []
    while heap:
        _, _, node, path = heapq.heappop(heap)
        if node in seen: continue
        seen.add(node)
        expanded.append(node)
        if node == goal:
            return path, expanded
        for nxt in graph.get(node, []):
            if nxt not in seen:
                heapq.heappush(heap, (h[nxt], next(tie), nxt, path + [nxt]))
    return None, expanded

graph = {'A':['B','C'], 'B':['D','E'], 'C':['F'],
         'D':['G'], 'E':['G'], 'F':['G'], 'G':[]}
h = {'A':6,'B':4,'C':3,'D':2,'E':2,'F':1,'G':0}
for name, result in [('BFS', bfs(graph,'A','G')),
                     ('DFS', dfs(graph,'A','G')),
                     ('Greedy', greedy_unweighted(graph,h,'A','G'))]:
    path, expanded = result
    print(f'{name:7}: path={path} | expanded={expanded} | count={len(expanded)}')
