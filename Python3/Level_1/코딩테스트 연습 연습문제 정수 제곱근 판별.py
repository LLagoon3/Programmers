def solution(n):
    if str(n**0.5)[-1] == '0': return int((n**0.5 + 1) ** 2)
    return -1

print(solution(121))


