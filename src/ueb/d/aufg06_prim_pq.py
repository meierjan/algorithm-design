from heapq import heappush, heappop

def prim_pq(G):
    m = len(G)
    p = [None]*m
    Q = [(float("inf"),u) for u in range(1,m)]
    heappush(Q,(0,0))
    T = set()
    c = 0

    while Q:

        (c_v,v) = heappop(Q)

        if not frozenset((p[v],v)) in T:
            T.add(frozenset((p[v],v)))
            c += c_v
            for u in set(G[v]) & {v for _,v in Q}:
                alt = G[v][u]
                if p[u] == None or alt < G[p[u]][u]:
                    heappush(Q,(alt,u))
                    p[u] = v
    return T-{frozenset((None,0))}, c      
