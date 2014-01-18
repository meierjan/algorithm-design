from ueb.c.aufg02_max_ks_exh import sol_max_ks, m_max_ks
from ueb.c.aufg02_max_ks_bt import K_max_ks



def o_max_ks(s,v,S,t):
    value = m_max_ks(s, v, S, t)
    for k in range(len(t),len(v)):
        value += v[k]
    return value

def max_ks_bab(s,v,S):
    m = len(s)
    opt = -1
    M = {()}
    while M:
        t_prev = M.pop()
        if o_max_ks(s,v,S,t_prev) > opt:
            for a in range(2):
                t = t_prev + (a,)
                if K_max_ks(s, v, S, t):
                    if len(t) == m:
                        c = m_max_ks(s, v, S, t)
                        if c > opt: opt = c
                    else:
                        if K_max_ks(s, v, S, t):
                            M.add(t)
                        else:
                            pass

    return opt
