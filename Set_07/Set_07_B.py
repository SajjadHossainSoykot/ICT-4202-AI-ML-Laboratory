"""ICT-4202 AI & ML Laboratory — Set 07, Question 2.
Greedy and misleading heuristic
Run: python Set_07/Set_07_B.py
"""

from collections import deque

import heapq

from itertools import count

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

graph={'S':['A','B','C'],'A':['D'],'B':['E'],'C':['F'],
       'D':['G'],'E':['G'],'F':['G'],'G':[]}
original_h={'S':7,'A':4,'B':5,'C':3,'D':2,'E':2,'F':1,'G':0}
misleading_h=dict(original_h)
misleading_h['A']=0   # Prefer A immediately despite the longer-looking D estimate.
misleading_h['D']=20  # Discourage finishing branch A-D, causing wasted expansion of A.
for label,h in [('Original',original_h),('Modified/misleading',misleading_h)]:
    path,expanded=greedy_unweighted(graph,h,'S','G')
    print(label,'heuristics:',h)
    print('  expanded:',expanded,'| count:',len(expanded),'| path:',path)
