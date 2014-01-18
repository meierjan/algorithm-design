def sol_max_ks(s,v,S,t):
    usedVolume = 0
    for i,isUsed in enumerate(t):
        if isUsed: usedVolume += s[i]
    return usedVolume <= S

def m_max_ks(s,v,S,t):
    value = 0
    for i,isUsed in enumerate(t):
        if isUsed: value += v[i]
    return value

from itertools import product
def max_ks_exhaustive(s,v,S):
    m = len(s)
    opt = -1
    y = product((0,1),repeat=m)

    for t in y:
        if sol_max_ks(s, v, S, t):
            t_value = m_max_ks(s, v, S, t)
            if  t_value > opt:
                opt = t_value
    return opt
