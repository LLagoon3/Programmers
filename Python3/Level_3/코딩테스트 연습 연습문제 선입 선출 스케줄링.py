def solution(n, cores):
    res, t, n = 0, 1, n - len(cores)
    while n != 0:
        for index, c in enumerate(cores):
            if t % c == 0: 
                n -= 1
                # print(index)
                res = index
        t += 1
        # print('====')
    return res + 1

def solution(n, cores):
    from math import gcd
    def lcm(narr):
        multmp, gcdtmp, lastnum = 1, 0, narr.pop()
        gcdtmp = lastnum
        for i in narr: 
            multmp, gcdtmp = multmp * i, gcd(gcdtmp, i)
        narr.append(lastnum)
        return (multmp * lastnum) // gcdtmp
    cycle, work_in_cycle = lcm(cores), 0
    for core in cores:
        work_in_cycle += cycle // core
    work, t, res = (n - len(cores)) % work_in_cycle, 1, 0
    while work != 0:
        for index, c in enumerate(cores):
            if t % c == 0: 
                work -= 1
                # print(index)
                res = index
        t += 1
        # print('====')
    return res + 1
        
def solution(n, cores):
    start, end = 0, 40000
    if n > len(cores): n -= len(cores)
    else: return n  
    while 1:
        mid, tmp, coretmp = (start + end) // 2, 0, 0
        for core in cores:
            tmp += (mid - 1) // core
        for i, core in enumerate(cores):
            if mid % core == 0:
                tmp += 1 
                coretmp = i + 1
            if tmp == n and coretmp != 0: 
                return coretmp
        if tmp >= n: end = mid
        else: start = mid

print(solution(5, [50, 50, 50, 30]))
                

