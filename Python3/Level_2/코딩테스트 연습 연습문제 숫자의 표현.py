def solution(n):
    from collections import deque
    res = 0
    s, cnt = 0, 1
    tmp = deque()
    while 1:
        if cnt > n: break
        elif s == n: 
            res += 1
            print(tmp)
            tmp.append(cnt)
            s += cnt
            cnt += 1 
        elif s > n: s -= tmp.popleft()  
        else:
            tmp.append(cnt)
            s += cnt
            cnt += 1 
    return res + 1

print(solution(15))
