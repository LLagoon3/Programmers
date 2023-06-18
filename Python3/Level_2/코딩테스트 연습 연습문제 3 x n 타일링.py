def solution(n):
    if n % 2 == 1: return 0
    me = {2: 3, 4: 11}
    for i in range(6, n + 2, 2):
        maxb = 0
        for j in range(2, (i // 2) + 1, 2):
            if i % j == 0 and maxb < j: maxb = j
        me[i] = ((me[maxb] ** (i // maxb)) + 2) % 1000000007
    return me[n]

print(solution(4))