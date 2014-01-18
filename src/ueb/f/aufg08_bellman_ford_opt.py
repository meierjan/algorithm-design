def bellman_ford_opt(G,s):
    m = len(G)
    opt = [None]*m
    last_v = [None]*m
    opt[s] = 0
    changed = False
    for _ in range(1,m):
        changed = False
        for v in range(m):

            for u in G[v]:
                if(opt[u]!=None):
                    alt = G[v][u] + opt[u]
                    if(opt[v] == None or alt<opt[v]):
                        opt[v] = alt
                        last_v[v] = u
                        changed = True
    if not changed: pass


    G_BF = [set() for _ in range(m)]
    for i in range(m):
        if last_v[i] != None:
            G_BF[last_v[i]].add(i)


    return opt, G_BF
