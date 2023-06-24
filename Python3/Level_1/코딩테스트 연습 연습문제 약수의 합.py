def solution(n):
    tmp = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: 
            tmp.add(i)
            tmp.add(n // i)
    print(tmp)
    return sum(tmp)

print(solution(1))