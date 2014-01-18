

def queen_backtracking_all(m):
    T = set()
    M = {()}
    while M:
        t_prev = M.pop()
        for a in range(m):       
            t = t_prev + (a,)
            if len(t) == m:
                if sol_queen(m,t):
                    T.add(t)
            else:
                if K_queen(m,t):
                    M.add(t)
                else:
                    pass
    return T
