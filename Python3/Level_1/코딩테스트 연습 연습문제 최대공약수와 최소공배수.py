def solution(n, m):
    res = [1, 0]
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0: res[0] = i
    res[1] = (n // res[0]) * (m // res[0]) * res[0]
    return res

print(solution(3, 12))