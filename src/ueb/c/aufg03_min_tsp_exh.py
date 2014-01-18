def m_min_tsp(m,D,p):
    cost = D[p[-1]][p[0]]
    current = 0
    for destination in range(1,len(p)):
        cost += D[p[current]][p[destination]]
        current = destination
    return cost


from itertools import permutations
def min_tsp_exhaustive(D):
    min = float("inf")
    m = len(D)
    C = permutations(range(0,m),m)
    for y in C:
        y_cost = m_min_tsp(m, D, y)
        if y_cost <= min: min = y_cost
    return min
