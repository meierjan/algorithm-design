
from vl.lek07.union_find import UnionFind

def kruskal(G):
    V = []
    T = set()
    cost = 0
    m = len(G)
    uf = UnionFind(m)
    for u,U in enumerate(G):
        for v in U:
            c_u_v = U[v]
            V.append((c_u_v,(u,v)))

    for e in sorted(V, key=lambda x: x[0]):
        c,(u,v) = e
        if(uf.find(u) != uf.find(v)):
            uf.union(uf.find(u), uf.find(v))
            T |= {frozenset((u,v))}
            cost += c
    return T, cost
