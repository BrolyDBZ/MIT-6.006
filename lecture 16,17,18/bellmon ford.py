def weight(key, v):
    return w[f'{key}{v}']


def bellmon_ford(s, Adj, edge):
    parent = {s: None}
    distance = {}
    for i in Adj.keys():
        if i == s:
            distance[i] = 0
        else:
            distance[i] = float('inf')
    for i in range(1, len(Adj.keys())):
        for edg in edge:
            if distance[edg[1]] > distance[edg[0]] + weight(edg[0], edg[1]):
                distance[edg[1]] = distance[edg[0]] + weight(edg[0], edg[1])
                parent[edg[1]] = edg[0]
    for edg in edge:
        if distance[edg[1]] > distance[edg[0]] + weight(edg[0], edg[1]):
            return f'There is negative edge_cycle between {edg[0]},{edg[1]}\n', parent, distance
    return parent, distance


w = {'ab': 10, 'ac': 3, 'bc': -8, 'cb': 4, 'cd': 8, 'bd': 2, 'ce': 2, 'de': 7, 'ed': 9}
Adj = {'a': ['c', 'b'], 'b': ['c', 'd'], 'c': ['b', 'e', 'd'], 'd': ['e'], 'e': ['d']}
ed = [('a', 'c'), ('a', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'b'), ('c', 'e'), ('c', 'd'), ('d', 'e'), ('e', 'd')]
print(bellmon_ford('a', Adj, ed))
