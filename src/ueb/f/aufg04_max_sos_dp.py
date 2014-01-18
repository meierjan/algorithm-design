
def max_sos_dp(s,S):
    m = len(s)

    M = [[0 for _ in range(S+1)] for _ in range(m+1)]
    for s_i,j in enumerate(range (1,m+1)):
        for w in range(len(M[j])):
            if(w==0):
                M[j][w] = 0
            elif s[s_i] > w:
                M[j][w] = M[j-1][w]
            else:
                M[j][w] = max(
                                M[j-1][w],
                                # s[s_i] + M[j-1][w-s[s_i]]
                                # BUT: (w-s[s_i]) can get < 0, so I use:
                                s[s_i] + M[j-1][max(0,(w-s[s_i]))]
                            )
    return max(M[-1])
