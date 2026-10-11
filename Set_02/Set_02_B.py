"""ICT-4202 AI & ML Laboratory — Set 02, Question 2.
Depth-Limited Search and IDDFS
Run: python Set_02/Set_02_B.py
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

graph = {'S':['A','B'],'A':['C','D'],'B':['E','F'],
         'C':['H'],'D':['G'],'E':['I'],'F':['J'],
         'G':[],'H':[],'I':[],'J':[]}
for limit in [2,3]:
    path,status,expanded = depth_limited_search(graph,'S','G',limit)
    print(f'DLS {limit}: status={status}; path={path}; expanded={expanded}')
path, iterations = print_iddfs(graph,'S','G',6)
assert path == ['S','A','D','G']
