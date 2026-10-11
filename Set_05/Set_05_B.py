"""ICT-4202 AI & ML Laboratory — Set 05, Question 2.
Greedy versus A*
Run: python Set_05/Set_05_B.py
"""

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

graph={'A':[('B',2),('C',3)],'B':[('D',4),('E',2)],
       'C':[('E',2)],'D':[('G',3)],'E':[('G',4)],'G':[]}
h={'A':6,'B':5,'C':4,'D':2,'E':3,'G':0}
greedy_path,greedy_cost,greedy_trace=greedy_weighted(graph,h,'A','G')
a_path,a_cost,a_trace=astar(graph,h,'A','G')
print('Greedy expanded (node,g,h):',greedy_trace,'| path:',greedy_path,'| cost:',greedy_cost)
print('A* expanded (node,g,h,f):',a_trace,'| path:',a_path,'| cost:',a_cost)
display_astar_trace(a_trace)
assert a_cost <= greedy_cost
