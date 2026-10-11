"""ICT-4202 AI & ML Laboratory — Set 03, Question 2.
A* and uniform-cost search
Run: python Set_03/Set_03_B.py
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

def display_astar_trace(trace):
    print("Node     g(n)     h(n)     f(n)")
    for node, g, h, f in trace:
        print(f"{node:>4} {g:>8} {h:>8} {f:>8}")

graph={'S':[('A',2),('B',4)],'A':[('C',2),('D',5)],
       'B':[('D',1)],'C':[('G',5)],'D':[('G',3)],'G':[]}
h={'S':6,'A':5,'B':4,'C':4,'D':2,'G':0}
path,cost,trace=astar(graph,h,'S','G')
display_astar_trace(trace)
print('A* path:',path,'| total cost:',cost)
h_zero={node:0 for node in h}
zero_path,zero_cost,zero_trace=astar(graph,h_zero,'S','G')
print('With h=0 (uniform-cost behavior):',zero_path,'| cost:',zero_cost)
display_astar_trace(zero_trace)
assert cost == zero_cost
