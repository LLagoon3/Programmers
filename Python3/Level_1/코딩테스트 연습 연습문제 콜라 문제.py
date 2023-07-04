def solution(a, b, n):
    res = 0
    while 1:
        tmp = n % a
        n = (n // a) * b
        print(n)
        res += n
        n +=  tmp
        if n < a: break
    return res
print(solution(3, 1, 20))