"""ICT-4202 AI & ML Laboratory — Set 06, Question 2.
BFS, DFS and IDDFS
Run: python Set_06/Set_06_B.py
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

def depth_limited_search(graph, start, goal, limit):
    """Return path, status (success/cutoff/failure), expanded sequence."""
    expanded = []
    def visit(node, path, depth):
        expanded.append((node, depth))
        if node == goal: return path, 'success'
        if depth >= limit:
            eligible = [v for v in graph.get(node, []) if v not in path]
            return None, ('cutoff' if eligible else 'failure')
        had_cutoff = False
        for nxt in graph.get(node, []):
            if nxt in path: continue
            result, status = visit(nxt, path + [nxt], depth + 1)
            if status == 'success': return result, status
            if status == 'cutoff': had_cutoff = True
        return None, 'cutoff' if had_cutoff else 'failure'
    path, status = visit(start, [start], 0)
    return path, status, expanded

def iddfs(graph, start, goal, max_depth=10):
    iterations = []
    for limit in range(max_depth+1):
        path, status, expanded = depth_limited_search(graph, start, goal, limit)
        iterations.append((limit, path, status, expanded))
        if status == 'success': break
        if status == 'failure': break
    return path, iterations

def print_iddfs(graph, start, goal, max_depth=10):
    path, iterations = iddfs(graph, start, goal, max_depth)
    for limit, candidate, status, expanded in iterations:
        trace = ' -> '.join(node for node, depth in expanded)
        print(f'Limit={limit} | status={status:7} | expanded={trace} | path={candidate}')
    print(f'IDDFS path: {path}; root visits: {len(iterations)}')
    return path, iterations

graph={'S':['A','B'],'A':['C','D'],'B':['E','F'],'C':['G'],
       'D':['H'],'E':['I'],'F':['J'],'G':[],'H':[],'I':[],'J':[]}
for name, fn in [('BFS',bfs),('DFS',dfs)]:
    path,trace=fn(graph,'S','G')
    print(f'{name}: path={path}; expanded={trace}; count={len(trace)}')
path,iterations=print_iddfs(graph,'S','G',8)
assert path==['S','A','C','G']
