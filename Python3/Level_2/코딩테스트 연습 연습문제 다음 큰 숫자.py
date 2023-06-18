
def encoding(n):
    res = []
    while n:
        res.append(n % 2)
        n = n // 2
    return res

def decoding(n):
    res = 0
    for i in range(0, len(n)):
        res += n.pop()*(2**i)
    return res

def solution(n):
    bn = encoding(n)
    chk = False
    cnt0, cnt1, i = 0, 0, 0
    for index, b in enumerate(bn):
        if chk and b == 0:
            i = index
            break
        if b == 1:
            chk = True
            cnt1 += 1
        elif b == 0: cnt0 += 1
        i = index
    l = len(bn) - 1
    res = []
    while bn:
        if l == i:
            res.append(1)
            res.append(0)
            for i in range(0, cnt0): res.append(0)
            for i in range(0, cnt1 - 1): res.append(1)
            break
        res.append(bn.pop())
        l -= 1
    return decoding(res)
    

print(solution(78))
        
        