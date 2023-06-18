
def solution(n):
    if n == 1: return 1
    res = [1, 2]
    for i in range(2, n):
        res.append((res[i - 1] + res[i - 2])% 1234567)
    return res[-1]

print(solution(2))