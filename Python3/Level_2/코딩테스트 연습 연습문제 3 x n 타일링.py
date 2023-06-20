def solution(n):
    if n % 2 == 1: return 0
    me = {2: 3, 4: 11}
    for i in range(6, n + 2, 2):
        maxb = 0
        for j in range(2, (i // 2) + 1, 2):
            if i % j == 0 and maxb < j: maxb = j
        me[i] = ((me[maxb] ** (i // maxb)) + 2) % 1000000007
    return me[n]

#Top Down
index = {0: 1, 2: 3}
def solution(n):
    if n % 2 != 0: return 0
    elif n == 0 or n == 2: return index[n]
    index[n] = (solution(n - 2)) * 3
    tmpn, tmpres = n - 4, 0
    for i in range(tmpn , -1, -2):
        tmpres += index[i] * 2
    index[n] = (index[n] + tmpres) % 1000000007
    return index[n] % 1000000007

#Bottom Up
index = {0: 1, 2: 3}
def solution(n):
    if n % 2 != 0: return 0
    elif n == 0 or n == 2: return index[n]
    for i in range(4, n + 1, 2):
        tmpres = 0
        for j in range(0, i - 3, 2):
            tmpres += index[j] * 2
        index[i] = (index[i - 2] * 3 + tmpres) % 1000000007
    print(index, tmpres)
    return index[n] % 1000000007

print(solution(10))