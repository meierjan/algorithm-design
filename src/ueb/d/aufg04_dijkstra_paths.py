
def dijkstra_paths(G,s):
    m = len(G)
    # predecessor list p
    p = [None]*m

    d = [None]*m                # (geschaetzte) Pfadkosten
    d[s] = 0                    # sind 0 fuer den Startknoten
    Q = {u for u in range(m)}   # alle Knoten
    while Q:
        # Auswahl von v mit kleinstem d-Wert
        (_,v) = min({(d[u],u) for u in Q if d[u]!= None})
        # v aus Q entfernen, d[v] ist endgueltig
        Q.remove(v)
        # Schaetzungen fuer Nachfolger von v aktualisieren
        for u in G[v]:
            alt = d[v] + G[v][u]            # alternative Kosten
            if d[u]==None or alt < d[u]:
                d[u] = alt
                # important:
                # only  change the predecessor if
                # you update the costs
                p[u] = v
    return d, p


def shortest_path(s,v,p):
    if(v == s):
        return [s]
    else:
        return shortest_path(s,p[v],p) + [v]
