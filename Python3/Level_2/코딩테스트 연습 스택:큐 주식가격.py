def solution(prices):
    res = []
    for i in range(0, len(prices)):
        tmp = 0
        for j in range(i + 1, len(prices)):
            tmp += 1
            if prices[i] > prices[j]:break
        res.append(tmp)
    return res

print(solution([3, 2, 1, 3, 2]))

def solution(prices):
    from collections import deque
    stk, res = [prices.pop()], deque([0])
    while prices:
        p = prices.pop()
        if p <= stk[-1]: res.appendleft(len(stk))
        else: res.appendleft(1)
        stk.append(p)
    return list(res)

def solution(prices):
    stk, res = [[0, prices[0], 0]], [0] * len(prices)
    for i in range(1, len(prices)):
        if prices[i] < stk[-1][1]: 
            cnt = 0
            while stk:
                tmp = stk.pop()   
                if tmp[1] > prices[i]:
                    cnt += 1
                    res[tmp[0]] = tmp[2] + cnt
                else: 
                    stk.append([tmp[0], tmp[1], tmp[2] + cnt])
                    break
        stk.append([i, prices[i], 0])
        # print(stk, res)
    for p in stk:
        res[p[0]] = len(prices) - p[0] - 1
    return res
            
print(solution([2, 3, 1, 2, 3]))
print(solution([3, 2, 1, 3, 2]))
print(solution([1, 2, 3, 2, 3]))