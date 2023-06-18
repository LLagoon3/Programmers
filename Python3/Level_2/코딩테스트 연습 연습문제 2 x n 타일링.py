n = 60000

def fac(a, b, c):
    res = 1
    if b > c: 
        ma = b
        mi = c
    else: 
        ma = c
        mi = b
    for i in range(ma + 1, int(a) + 1):
        res = res * i
        if i - ma <= mi: res = res // (i - ma) 
    # print(a, b, c, ' : ', res)
    return res

def solution_(n):
    a, answer = 1, 1
    if n % 2 == 0:
        answer += 1
        a = 2
    for i in range(a, n, 2):
        b = (((n - i) // 2) + i)
        res = fac(b, i, b - i)
        answer += res
        # fac_dic = res[1]
    return int(answer) % 1000000007

def solution(n):
    a, res = 1, 0
    if n % 2 == 0:
        res += 1
        a = 2
    b = (((n - a) // 2) + a)
    c = b - a
    back = fac(b, a, c)
    res += back 
    for i in range(1, n - b + 1):
        tmp = (back * (b + 1)) * c
        tmp = tmp // ((a + 1) * (a + 2))
        b += 1
        a += 2
        c -= 1
        back = tmp 
        res += tmp
        res = res % 1000000007
    return res

print(solution(n))