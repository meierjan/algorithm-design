from vl.lek03.dfs import dfs

def comp(G):
    V = {i for i in range(len(G)) }
    C = []
    while V:
        v = V.pop()
        E,_ = dfs(G, v)
        C.append(E)
        V  -= E
    return C
