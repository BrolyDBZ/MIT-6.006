def dfs_visit(Adj, s, parent):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(Adj, v, parent)


def dfs(Adj):
    parent = {}
    for s in Adj.keys():
        if s not in parent:
            parent[s] = None
            dfs_visit(Adj, s, parent)
    return parent


Adj = {'r': ['s', 't'], 's': ['t', 'x'], 't': ['x', 'y', 'z'], 'x': ['y', 'z'], 'y': ['z'], 'z': []}
print(dfs(Adj))
