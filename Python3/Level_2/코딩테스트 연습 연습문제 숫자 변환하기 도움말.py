def solution(x, y, n):
    from collections import deque
    q, cnt = deque(), 0
    q.append([x, 0])
    while q:
        print(q)
        tmp = q.popleft()
        if cnt >= 3: return -1
        if tmp[0] > y: cnt += 1
        else: cnt = 0
        if y in [tmp[0] + n, tmp[0] * 2, tmp[0] * 3]: 
            return tmp[1] + 1
        q.append([tmp[0] + n, tmp[1] + 1])
        q.append([tmp[0] * 2, tmp[1] + 1])
        q.append([tmp[0] * 3, tmp[1] + 1])
    return cnt

def solution(x, y, n):
    if x == y: return 0
    from collections import deque
    q = deque()
    q.append([x, 0])
    while q:
        tmp = q.popleft()
        res = [tmp[0] + n, tmp[0] * 2, tmp[0] * 3]
        if y in res: 
            return tmp[1] + 1
        for i in res:
            if i < y: q.append([i, tmp[1] + 1])
    return -1

def solution(x, y, n):
    if x == y: return 0
    from collections import deque
    q = deque()
    q.append([y, 0])
    while q:
        tmp = q.popleft()
        res = [tmp[0] - n]
        if tmp[0] % 2 == 0: res.append(tmp[0] // 2)
        if tmp[0] % 3 == 0: res.append(tmp[0] // 3)
        if x in res: 
            return tmp[1] + 1
        for i in res:
            if i > x: q.append([i, tmp[1] + 1])
    return -1

print(solution(1,11, 1))
