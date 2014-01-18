from ueb.c.aufg03_min_tsp_exh import m_min_tsp

def u_min_tsp(D,p):
    if len(p) == 0: return 0
    cost = 0
    current = 0
    for destination in range(1,len(p)):
        cost += D[p[current]][p[destination]]
        current = destination
    return cost

def min_tsp_bab(D):
    opt = float("inf")
    m = len(D)
    M = [()]
    while M:
        t_prev = M.pop()
        if u_min_tsp(D,t_prev) < opt:
            for a in range(m):
                t = t_prev + (a,)
                if len(t) == len(set(t)):
                    if len(t) == m:
                            t_value = m_min_tsp(m, D, t)
                            if(t_value < opt): opt = t_value
                    else:
                        M.append(t)


    return opt
