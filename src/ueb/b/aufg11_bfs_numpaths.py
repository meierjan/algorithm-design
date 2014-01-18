from vl.lek03.bfs import bfs

def bfs_numpaths(G,s):
    L,P = bfs(G, s)
    S = [0 for _ in G]
    S[s] = 1
    for i in range(1,len(L)):
        for u in L[i]:
            for v in L[i-1]:
                if(u in G[v]):
                    S[u] += S[v]

    return S
