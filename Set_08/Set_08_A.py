"""ICT-4202 AI & ML Laboratory — Set 08, Question 1.
DLS and IDDFS
Run: python Set_08/Set_08_A.py
"""

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

graph={'A':['B','C'],'B':['D','E'],'C':['F'],
       'D':['H'],'E':['I'],'F':['G'],'G':[],'H':[],'I':[]}
for limit in [2,3]:
    path,status,expanded=depth_limited_search(graph,'A','G',limit)
    print(f'DLS(limit={limit}): status={status}; path={path}; trace={expanded}')
path,iterations=print_iddfs(graph,'A','G',8)
root_visits=sum(node=='A' for limit,p,status,tr in iterations for node,depth in tr)
print('Direct count of root visits across DLS iterations:',root_visits)
assert path==['A','C','F','G']
