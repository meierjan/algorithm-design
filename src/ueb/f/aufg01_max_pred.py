
# uses merge
from ueb.a.aufg05_merge import merge

def max_predecessors(L):
    m = len(L)
    # initalize all predecessors as -1 (no predecessor)
    p = [-1 for _ in range(m)]
    # create list of all intervals in L
    # as triples (interval_start_time, interval_index, True) (True = is start time triple)
    # sort by interval_start_time
    S = sorted([(interval[0],i,True) for i,interval in enumerate(L)])
    # create list of all intervals in L
    # as triples (interval_finish_time, interval_index, False) (False = is end time triple)
    F = [(interval[1],i,False) for i,interval in enumerate(L)]

    # merge lists S and F) to merged_list
    # merged_lists has now sorted tripled by start/end time
    merged_list = merge(S, F)

    # keep the interval index of the triple in mind with
    # the last finish time so far
    # as we initialize it: no triple index -> -1
    last_f = -1
    for element in merged_list:
        _,interval_index,isStartElement = element
        # if its a triple with starting times ...
        if isStartElement:
            # the predecessor is the tuple we kept in mind with the last fiinish time
            p[interval_index] = last_f
        # else (its a triple with a finish time)
        else:
            # keep it in mind as the last finish time we have so far
            last_f = interval_index


    return p
