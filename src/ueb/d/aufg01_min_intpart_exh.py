def compatible(L,M):
    deadline = -1
    for i in M:
        s,f = L[i]
        if s < deadline:
            print (L[i],deadline)
            return False
        deadline = f
    return True

def sol_min_intpart(L,r):
    for R in r:
        if not compatible(L, R): return False
    return True

def m_min_intpart(L,r):
    resources = 0
    for R in r:
        if(len(R)!=0): resources += 1
    return resources

from itertools import product

def min_intpart_exhaustive(L):
    m = len(L)
    C = []
    opt = m

    for order in product(*[range(i) for i in range(1,m+1)]):
        # create new list with m resources
        candidate = [[] for _ in range(m)]
        # c_i    index of intervals
        # r_i    resource for interval
        # put each interval in the target resource
        for c_i, r_i in enumerate(order):
            candidate[r_i].append(c_i)
        C.append(candidate)

        for y in C:
            if sol_min_intpart(L, y):
                value = m_min_intpart(L, y)
                if value < opt:
                    opt = value
    return opt
