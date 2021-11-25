def bfs(s, Adj):
    parent = {s: None}
    level = {s: 0}
    bucket = [s]
    while bucket:
        temp = []
        for u in bucket:
            for v in Adj[u]:
                if v not in parent:
                    parent[v] = u
                    level[v] = level[u.parent] + 1
                    temp.append(v)
        bucket = temp
    return (parent, level)
