def solution(N):
    return sum(list(int(i) for i in str(N)))

def solution(N):
    res, cnt = 0, 0
    while 1:
        cnt += 1
        tmp = N % (10 ** cnt)
        if tmp == 0: break
        N -= tmp
        res += tmp // (10 ** (cnt - 1))
    return res


print(solution(5275))