from ueb.d.aufg07_kruskal import kruskal
from ueb.b.aufg12_comp import comp

def cluster(m,d,l):

    G = [{} for _ in range(m)]
    for u in range(m):
        for v in range(m):
            if d[u,v] != 0:
                G[u][v] = d[u,v]

    T,_ = kruskal(G)

    if l>1:
        def f(x) : u,v = x;  return d[u,v]
        for v in sorted(T, key=f)[-(l-1):]:
            T.remove(v)

    G = [set() for _ in range(m)]
    for u,v in T:
        G[u].add(v)
        G[v].add(u)
    C = comp(G)

    return C
