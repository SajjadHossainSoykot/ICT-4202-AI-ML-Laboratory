"""ICT-4202 AI & ML Laboratory — Set 04, Question 1.
BFS, DFS and bidirectional search
Run: python Set_04/Set_04_A.py
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

from collections import deque

def bidirectional_search(graph, start, goal):
    """BFS forward on directed edges and backward on their reversed edges."""
    if start == goal: return [start], [('forward', start)]
    reverse = {u: [] for u in graph}
    for u, neighbors in graph.items():
        for v in neighbors:
            reverse.setdefault(v, []).append(u)
    f_queue, b_queue = deque([start]), deque([goal])
    forward_paths, backward_paths = {start:[start]}, {goal:[goal]}
    trace = []
    while f_queue and b_queue:
        for direction, queue, own, other, adjacency in [
            ('forward', f_queue, forward_paths, backward_paths, graph),
            ('backward', b_queue, backward_paths, forward_paths, reverse),
        ]:
            for _ in range(len(queue)):
                node = queue.popleft()
                trace.append((direction, node))
                if node in other:
                    return forward_paths[node] + backward_paths[node][1:], trace
                for nxt in adjacency.get(node, []):
                    if nxt in own: continue
                    own[nxt] = (own[node] + [nxt]) if direction == 'forward' else ([nxt] + own[node])
                    queue.append(nxt)
                    if nxt in other:
                        return forward_paths[nxt] + backward_paths[nxt][1:], trace
    return None, trace

graph={'P':['Q','R'],'Q':['S','T'],'R':['U'],'S':['V'],
       'T':['V'],'U':['V'],'V':[]}
for label, fn in [('BFS',bfs),('DFS',dfs)]:
    path, expanded = fn(graph,'P','V')
    print(f'{label}: path={path}; expanded={expanded}; expanded count={len(expanded)}')
bidir_path,bidir_trace=bidirectional_search(graph,'P','V')
print('Bidirectional:',bidir_path,'| expansion order (direction, node):',bidir_trace,
      '| expanded count:',len(bidir_trace))
changed={k:list(v) for k,v in graph.items()}
changed['Q']=list(reversed(changed['Q']))
print('DFS with Q children reversed:',dfs(changed,'P','V'))
