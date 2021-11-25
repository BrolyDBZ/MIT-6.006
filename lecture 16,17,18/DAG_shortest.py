def weight(key, v):
    return w[f'{key}{v}']


def path_visit(Adj, s, parent, distance):
    for v in Adj[s]:
        if distance[v] > distance[s] + weight(s, v):
            distance[v] = distance[s] + weight(s, v)
            parent[v] = s
            path_visit(Adj, v, parent, distance)


def path(s, Adj):
    parent = {s: None}
    distance = {}
    for i in Adj.keys():
        if i == s:
            distance[i] = 0
        else:
            distance[i] = float('inf')
    for v in Adj[s]:
        path_visit(Adj, s, parent, distance)
    return parent, distance


Adj = {'r': ['s', 't'], 's': ['t', 'x'], 't': ['x', 'y', 'z'], 'x': ['y', 'z'], 'y': ['z'], 'z': []}
w = {'rs': 5, 'rt': 3, 'st': 2, 'sx': 6, 'tx': 7, 'ty': 4, 'tz': 2, 'xy': -1, 'xz': 1, 'yz': -2}

print(path('r', Adj))
