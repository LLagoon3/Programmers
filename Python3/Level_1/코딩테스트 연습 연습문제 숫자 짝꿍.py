def solution(X, Y):
    from collections import Counter
    x, y, num, res = dict(Counter(list(X))), dict(Counter(list(Y))), dict(), ''
    for xkey, xval in x.items():
        if xkey in y.keys(): num[xkey] = min(xval, y[xkey])
    num = sorted(num.items(), reverse= True)
    if not num: return "-1"
    elif num[0][0] == '0': return "0"
    for n in num:
        for i in range(0, n[1]):
            res += n[0]
            
    return res
    
print(solution("12321", "42531"))
    