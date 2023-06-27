n, l, r = 5, [2, 4], [1, 3, 5]

def solution(n, lost, reserve):
    st, res = [1] * (n + 2), 0
    st[0], st[-1] = 0, 0
    for i in range(1, n + 1):
        if i in lost: st[i] -= 1
        if i in reserve: st[i] += 1
    for i in range(1, n + 1):
        if st[i] == 0:
            if st[i - 1] == 2: st[i - 1], st[i] = 1, 1
            elif st[i + 1] == 2: st[i + 1], st[i] = 1, 1
    for s in st:
        if s > 0: res += 1
    print(st)
    return res

print(solution(n, l, r))