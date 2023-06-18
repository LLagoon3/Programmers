def solution(a, b):
    res = 0
    for i in range(min(a, b), max(a, b) + 1): res += i
    return res

print(solution(3, 3))