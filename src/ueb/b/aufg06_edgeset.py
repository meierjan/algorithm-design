def edgeset(G):
    E = set()
    for i,u in enumerate(G):
        for v in u:
            E.add(frozenset({i,v}))
    return E

def edgeset_di(G):
    E = set()
    for i,u in enumerate(G):
        for v in u:
            E.add((i,v))
    return E
