def solution(n):
    return list(reversed(list(map(lambda x : int(x), str(n)))))

print(solution(12345))
