from ueb.b.aufg12_comp import comp

def comp_di(G):
    G_ungerichtiet = [set() for _ in G]
    for u,U in enumerate(G):
        for v in U:
            G_ungerichtiet[v].add(u)
            G_ungerichtiet[u].add(v)

    return comp(G_ungerichtiet)
