def solution(name):
    name, index, ptr, res = list(map(lambda x : x if x != 'A' else '*', name)), dict(), 0, 0
    for i in range(0, 26): index[chr(65 + i)] = i
    while 1:
        print(name, ptr, res)
        if ptr == -1: break
        elif name[ptr] != '*': res, name[ptr] = res + min(index[name[ptr]], 26 - index[name[ptr]]), '*'
        lptr, rptr, cnt = ptr, ptr, 0
        while 1:
            tmplptr, tmprptr, cnt = (lptr - 1) if lptr != 0 else len(name) - 1, (rptr + 1) if rptr != len(name) - 1 else 0, cnt + 1
            if cnt >= len(name): ptr = -1
            elif name[tmprptr] != '*':  ptr, res = tmprptr, res + cnt
            elif name[tmplptr] != '*': ptr, res = tmplptr, res + cnt
            else: 
                lptr, rptr = tmplptr, tmprptr
                continue
            break
    return res

def dfs(name, index):
    from copy import deepcopy
    stk, tmpname, res = [[0, 0, []]], deepcopy(name), 100
    while stk:
        ptr, cnt, v = stk.pop()
        if ptr in v: 
            if len(v) == len(name):
                while v:
                    if name[v[-1]] == 'A':
                        cnt -= 1
                        v.pop()
                    else: break
                res = min(res, cnt)
                print('res: ', res, ' cnt : ', cnt)
            continue
        cnt += min(index[tmpname[ptr]], 26 - index[tmpname[ptr]]) + 1
        lptr, rptr = (ptr - 1) if ptr != 0 else len(name) - 1, (ptr + 1) if ptr != len(name) - 1 else 0
        tmpv = deepcopy(v)
        tmpv.append(ptr)
        stk.extend([[lptr, cnt, tmpv], [rptr, cnt, tmpv]])
        print(stk)
    print(res)
    
def solution(name):
    name, index = list(name), dict()
    for i in range(0, 26): index[chr(65 + i)] = i
    dfs(name, index)

def solution(name):
    stk, res, index, answer = [], [0, 0, 0], dict(), 0
    for i in range(0, 26): index[chr(65 + i)] = i
    for i in range(0, len(name)):
        if name[i] == 'A': stk.append(i)
        else:
            if not stk: continue
            elif res[2] < i - stk[0]:
                res = [stk[0], i, i - stk[0]]
    if res[2] != 0: name, answer = name[res[1]:] + name[:res[0]], (len(name) - res[1] - 1) * 2
    print(name, res, answer)
    for i in name:
        answer += min(index[i], 26 - index[i])
    return answer + len(name) - 1

def cqueueIndex(i):
    if i < 0: return length + i
    return i % length

def calNextIndex(name, i):
    rp, rcnt, lp, lcnt = i, 0, i, 0
    while rcnt < length:
        rp = cqueueIndex(rp + 1)
        rcnt += 1
        if name[rp] != 'A': break
    while lcnt < length:
        lp = cqueueIndex(lp - 1)
        lcnt += 1
        if name[lp] != 'A': break
    if rcnt > lcnt: return (lp, lcnt)
    elif rcnt < lcnt: return (rp, rcnt)
    else: return (-1, 0)
    
def calChangeAlpha(a):
    tmp = abs(65 - ord(a))
    return min(tmp, abs(26 - tmp))

def solution(name):
    global length 
    name, length, res, index = list(name), len(name), 0, 0
    while 1:
        tmp = calNextIndex(name, index)
        res += calChangeAlpha(name[index]) + tmp[1]
        name[index], index = 'A', tmp[0]
        if index == -1: break
    return res
        
        

print(solution("BBBBAAAABA"))
# print(solution("AAAAAB"))

# t = list("BBBBAAAABA")
# global length
# length = len(t)
# print(calNextIndex(t, 8))