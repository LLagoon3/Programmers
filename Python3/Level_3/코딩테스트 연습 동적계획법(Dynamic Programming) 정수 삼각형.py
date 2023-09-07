def solution(triangle):
    from copy import deepcopy
    stmp = [triangle[0][0]]
    for h in triangle:
        tmp, maxn = [], 0
        if len(h) == 1: continue
        for i in range(0, len(h)):
            l, r = 0, 0
            if i - 1 >= 0:
                l = stmp[i - 1] + h[i]
            if i < len(stmp):
                r = stmp[i] + h[i]
            n = max(l, r)
            if n > maxn: maxn = n
            tmp.append(n)
        stmp = deepcopy(tmp)
    return maxn

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
            