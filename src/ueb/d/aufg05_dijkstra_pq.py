
from heapq import heappush, heappop
import heapq

def dijkstra_pq(G,s):
    m = len(G)
    d = [float("inf")]*m
    p = [None]*m
    d[s] = 0
    Q = [(d[x],x) for x in range(m)]

    while Q:
        c,v = heappop(Q)
        for u in G[v]:
            alt = d[v] + G[v][u]
            if d[u]==None or alt < d[u]:
                d[u] = alt
                heappush(Q, (alt,u))
    return d
