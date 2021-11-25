from MinHeap import Heap


def dijkstra(Adj, s):
    parent = {s: None}
    distance = {}
    heap = Heap()
    for i in Adj.keys():
        if i == s:
            distance[i] = 0
            heap.insert((i, 0))
        else:
            distance[i] = float('inf')
            heap.insert((i, float('inf')))
    while len(heap.key) > 0:
        key = heap.delete()[0]
        for v in Adj[key]:
            if distance[v] > distance[key] + weight(key, v):
                distance[v] = distance[key] + weight(key, v)
                parent[v] = key
                heap.table[heap.key[v]] = (v, distance[v])
                heap.decrease(heap.key[v])
    return parent, distance


def weight(key, v):
    return w[f'{key}{v}']


w = {'ab': 10, 'ac': 3, 'bc': 1, 'cb': 4, 'cd': 8, 'bd': 2, 'ce': 2, 'de': 7, 'ed': 9}
Adj = {'a': ['c', 'b'], 'b': ['c', 'd'], 'c': ['b', 'e', 'd'], 'd': ['e'], 'e': ['d']}
print(dijkstra(Adj, 'a'))
