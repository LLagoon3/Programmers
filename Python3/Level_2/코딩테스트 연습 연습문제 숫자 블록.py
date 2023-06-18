def solution(begin, end):
    res = []
    for i in range(begin, end + 1):
        n = 1
        if i == 1:
            res.append(0)
            continue
        for j in range(i // 2, 0, -1):
            if i % j == 0:
                n = j
                break
        res.append(n)
    return res

def solution(begin, end):
    res = []
    import math
    for i in range(begin, end + 1):
        n = 1
        maxj = 0
        if i == 1:
            res.append(0)
            continue
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                maxj = j
                n = i // j
                if n <= 10000000:
                    break
        if n > 10000000: n = maxj
        res.append(n)
    return res
        
print(solution(100000014, 100000016))