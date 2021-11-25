from MinHeap import Heap


def edge(u, v, w):
    if f'{u}{v}' in w.keys():
        return True
    return False


def weight(u, v, w):
    return w[f'{u}{v}']


def dijkstra(Adj, s, t, fweight, RAdj, Bweight):
    parent = {s: None}
    Rparent = {t: None}
    distance = {}
    Rdistance = {}
    fheap = Heap()   # forward heap
    bheap = Heap()   # backward heap
    mu = float('inf')
    for i in Adj.keys():   # intialization
        if i == s:
            fheap.insert((i, 0))
            bheap.insert((i, float('inf')))
            distance[i] = 0
            Rdistance[i] = float('inf')
        elif i == t:
            fheap.insert((i, float('inf')))
            bheap.insert((i, 0))
            distance[i] = float('inf')
            Rdistance[i] = 0
        else:
            fheap.insert((i, float('inf')))
            bheap.insert((i, float('inf')))
            distance[i] = float('inf')
            Rdistance[i] = float('inf')
    while len(fheap.key) > 0 or len(bheap.key) > 0:
        fkey = fheap.delete()[0]
        bkey = bheap.delete()[0]
        # checking wheather there edge between forward extract and backward extract and find the path between them
        if fkey != bkey and edge(fkey, bkey, fweight):
            if mu > distance[fkey] + Rdistance[bkey] + weight(fkey, bkey, fweight):
                mu = distance[fkey] + Rdistance[bkey] + weight(fkey, bkey, fweight), fkey, bkey
        # stop condition when forward extract is equal to bakcward extract
        if fkey == bkey:
            # checking whether there is extracted node from stop condition in shortest path or not
            if distance[fkey] + Rdistance[bkey] > mu[0]:
                array = []
                Rarray = []
                iter = mu[1]
                Riter = mu[2]
                while iter is not None:
                    print()
                    array.append(iter)
                    iter = parent[iter]
                while Riter is not None:
                    Rarray.append(Riter)
                    Riter = Rparent[Riter]
                array.reverse()
                array.extend(Rarray)
                return mu[0], array
            else:
                array = []
                Rarray = []
                iter = fkey
                Riter = Rparent[bkey]
                while iter is not None:
                    array.append(iter)
                    iter = parent[iter]
                while Riter is not None:
                    Rarray.append(Riter)
                    Riter = Rparent[Riter]
                array.reverse()
                array.extend(Rarray)
                return distance[fkey] + Rdistance[bkey], array
        for v in Adj[fkey]:
            if distance[v] > distance[fkey] + weight(fkey, v, fweight):
                distance[v] = distance[fkey] + weight(fkey, v, fweight)
                parent[v] = fkey
                fheap.table[fheap.key[v]] = (v, distance[v])
                fheap.decrease(fheap.key[v])
        for v in RAdj[bkey]:
            if Rdistance[v] > Rdistance[bkey] + weight(bkey, v, Bweight):
                Rdistance[v] = Rdistance[bkey] + weight(bkey, v, Bweight)
                Rparent[v] = bkey
                bheap.table[bheap.key[v]] = (v, Rdistance[v])
                bheap.decrease(bheap.key[v])



Adj = {'s': ['u', 'w'], 'w': ['t'], 'u': ['u1'], 'u1': ['t'], 't': []}
RAdj = {'t': ['u1', 'w'], 'w': ['s'], 'u1': ['u'], 'u': ['s'], "s": []}
fweight = {'sw': 5, 'su': 3, 'uu1': 4, 'u1t': 3, 'wt': 5}
bweight = {'tw': 5, 'tu1': 3, 'u1u': 3, 'us': 3, 'ws': 5}
print(dijkstra(Adj, 's', 't', fweight, RAdj, bweight))
