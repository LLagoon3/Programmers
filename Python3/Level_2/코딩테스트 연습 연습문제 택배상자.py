def solution(order):
    npos, res, tmp = 0, 0, []
    for i in range(1, len(order) + 1):
        if order[npos] == i:
            npos, res = npos + 1, res + 1
        elif (tmp != []) and order[npos] == tmp[-1]:
            npos, res = npos + 1, res + 1
            tmp.pop()
        else:
            tmp.append(i)
    while tmp:
        if order[npos] == tmp.pop():
            npos, res = npos + 1, res + 1
        else: break
    return res

def solution(order):
    from collections import deque
    num, tmp, npos, res = deque([i for i in range(1, len(order) + 1)]), deque(), 0, 0
    while num or tmp:
        if num and order[npos] == num[0]:
            num.popleft()
            res, npos = res + 1, npos + 1
        elif tmp and order[npos] == tmp[0]:
            tmp.popleft()
            res, npos = res + 1, npos + 1
        else:
            if not num: break
            tmp.appendleft(num.popleft())
    return res        
    
print(solution([5, 4, 3, 2, 1]))