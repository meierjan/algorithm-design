
def dfs_rec(G, u, explored = None):
    if(not explored):
        explored = [False for _ in G]
    # u is visited because we are looking at it now
    explored[u] = True
    # for all adjacent vertices...
    for v in G[u]:
        # that are not already visited ...
        if not explored[v]:
            # look @ the subtree
            explored = dfs_rec(G,v,explored)
    # return explored list
    return explored
