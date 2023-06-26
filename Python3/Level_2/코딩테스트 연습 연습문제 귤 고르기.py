t = [1, 3, 2, 5, 4, 5, 2, 3]

def solution(k, tangerine):
    from collections import Counter 
    dic= dict(Counter(tangerine))
    slist = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    for i in range(0, len(slist)):
        k -= slist[i][1]
        if k <= 0: break
    return i + 1
    
print(solution(6, t))

