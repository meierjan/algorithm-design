# MAX WEIGHTED INTERVAl SCHEDULING

from ueb.f.aufg01_max_pred import max_predecessors

# Bestimme A_opt rekursiv
def find_sol(j, opt, p, A = None):
    if(j!=-1):
        if(j>0 and opt[j]==opt[j-1]):
            return find_sol(j-1, opt, p, A)
        else:
            A.add(j)
            return find_sol(p[j], opt, p, A)
    return A

# Dynamic Programming

def max_weighted_intsched_dp_sol(L):
    m = len(L)
    p = max_predecessors(L)
    opt = [-1 for _ in range(m)]
    for j,(_,_,v) in enumerate(L):
        if(p[j] == -1):
            opt[j] = v
        else:
            opt[j] = max(opt[p[j]]+v,opt[j-1])

    return find_sol(m-1,opt,p,set())
