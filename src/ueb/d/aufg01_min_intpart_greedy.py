from ueb.d.aufg01_min_intpart_exh import compatible, m_min_intpart

def min_intpart_greedy(L):

    m = len(L)
    # create m resources
    R = [[] for _ in range(m)]
    for i,_ in enumerate(L):
        for r in R:
            # if current resource intersected with new
            # element is compatible -> add it
            # else try next resource
            if(compatible(L, r + [i])):
                r.append(i)
                break;
    print(R)
    return m_min_intpart(L, R)
