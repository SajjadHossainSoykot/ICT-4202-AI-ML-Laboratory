"""ICT-4202 AI & ML Laboratory — Set 09, Question 2.
A* heuristic admissibility
Run: python Set_09/Set_09_B.py
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

graph={'S':[('A',1),('B',5)],'A':[('C',2),('D',4)],
       'B':[('D',1)],'C':[('G',5)],'D':[('G',2)],'G':[]}
# True remaining costs: S=7, A=6, B=3, C=5, D=2, G=0.
# The base heuristic never overestimates these true values.
h={'S':6,'A':5,'B':3,'C':4,'D':2,'G':0}
true_to_goal={'S':7,'A':6,'B':3,'C':5,'D':2,'G':0}
print('Admissibility check (h <= optimal remaining cost):')
for node in h:
    print(node,'h=',h[node],'true remaining=',true_to_goal[node],
          'admissible=',h[node]<=true_to_goal[node])
optimal_path,optimal_cost,trace=astar(graph,h,'S','G')
print('\nA* with admissible h:',optimal_path,'| total cost:',optimal_cost)
display_astar_trace(trace)
bad_h=dict(h);bad_h['A']=100  # deliberately overestimates A's true cost-to-go (6)
bad_path,bad_cost,bad_trace=astar(graph,bad_h,'S','G')
print('A* with nonadmissible h(A)=100:',bad_path,'| total cost:',bad_cost)
display_astar_trace(bad_trace)
assert optimal_cost==7
assert bad_cost>=optimal_cost
