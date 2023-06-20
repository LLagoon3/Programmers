def solution(n, k):
    nfac = 1
    res, index = [], [1]
    for i in range(2, n + 1): 
        nfac *= i
        index.append(i)
    tmpfac = nfac
    for i in range(0, n):
        tmpfac //= (n - i) # n - i fac
        cnt = 1
        for a in index:
            if a in res: continue
            elif k > (cnt - 1)*tmpfac and k<= cnt*tmpfac:
                res.append(a)
                k -= (cnt - 1)*tmpfac
                break
            cnt += 1
    return res

print(solution(3, 1))     