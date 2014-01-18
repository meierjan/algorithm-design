from collections import deque

def bfs_queue(G,s):
    # empty parent array
    parent = [None for _ in G]
    # is node x already reached?
    # (without: cant say if startnode or not reached)
    reached = [False for _ in G]
    # only start vertex is reached
    reached_v = {s}
    # add start vertex to deque
    q= deque([s])
    # start node is reached
    reached[s] = True

    while len(q):
        u = q.popleft()
        for v in G[u]:
            if(not reached[v]):
                reached[v] = True
                parent[v] = u
                q.append(v)
                reached_v.add(v)
    return reached_v, parent
