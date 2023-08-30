def solution1(r1, r2):
    res, restmp = 0, 0
    for x in range(int(r1 / (2 ** 0.5)), r2):
        for y in range(1, x):
            tmp = ((x ** 2) + (y ** 2)) ** 0.5
            if r1 <= tmp <= r2:
                res += 1
        if r1 <= ((x ** 2) + (x ** 2)) ** 0.5 <= r2: 
            restmp += 1
    # print(res, restmp)
    return (res * 8) + (restmp * 4) + ((r2 - r1 + 1) * 4)

def solution(r1, r2):
    from math import sqrt, pow
    res = 0
    for x in range(1, r2):
        if x <= r1: r1y = sqrt((pow(r1, 2)) - (pow(x, 2)))
        else: r1y = 0
        r2y = sqrt(pow(r2, 2) - pow(x, 2))
        tmp = res
        if r1y == 0: res += 1
        elif r1y % 1 == 0 and r2y % 1 == 0: res += 1
        res += int(r2y) - int(r1y)
        print(x, r1y, r2y, res - tmp)
    res += 1
    print(res)
    return (res * 4)

def solution(r1, r2):
    import math
    res = 0
    
    def ry(rx, x):
        if rx <= x: return 0
        y = ((rx ** 2) - (x ** 2)) ** 0.5
        return y
    
    def count(start, end):
        count = math.floor(end) - math.ceil(start) + 1
        return max(count, 0)
    
    for x in range(1, r2 + 1):
        r1y, r2y = ry(r1, x), ry(r2, x)
        # if r2y != 0 and r2y % 1 == 0: res += 1
        # print(r2y, r1y, count(r1y, r2y))
        res += count(r1y, r2y)
    return res * 4

print(solution1(99, 100))
print(solution(99, 100))
print(solution(2, 3))
