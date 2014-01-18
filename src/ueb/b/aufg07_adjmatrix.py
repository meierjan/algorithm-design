def to_matrix(G):
    A = [[0 for _ in G] for _ in G]
    for u,V in enumerate(G):
        for v in V:
            A[u][v] = 1
    return A

def from_matrix(A):
    G = [set() for _ in A]
    for u,U in enumerate(A):
        for v,isAdjacent in enumerate(U):
            if(isAdjacent):
                G[u].add(v)
    return G
