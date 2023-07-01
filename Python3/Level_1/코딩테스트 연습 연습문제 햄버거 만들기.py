i = [2, 1, 1, 2, 3, 1, 2, 3, 1]
i = [1, 1, 2, 3, 1, 2, 3, 1]
# i = [1, 3, 2, 1, 2, 1, 3, 1, 2]

def solution(ingredient):
    s, res = ''.join(list(map(str, ingredient))), 0
    tmp = 1 if '1231' in s else 0
    while tmp != 0:
        print(s)
        res += 1
        s = s.replace('1231', '', 1)
        tmp = 1 if '1231' in s else 0
    return res

def solution(ingredient):
    stk, res, i = [], 0, 0
    while i < len(ingredient):
        print(ingredient, stk)
        if ingredient[i] == 0: 
            i += 1
            continue
        elif not stk: stk.append([i, ingredient[i]])
        elif ingredient[i] == 1:
            if stk and stk[-1][1] == 3:
                for tmp in stk: ingredient[tmp[0]] = 0
                res += 1
                stk, ingredient[i] = [], 0
                i = 0
                continue
            else:
                stk = [[i, 1]]
        elif ingredient[i] == stk[-1][1] + 1:
            stk.append([i, ingredient[i]])
        i += 1
    return res

def solution(ingredient):
    index, olist, cnt = [], [], 0
    while 1:
        if ingredient[cnt] == 1:
            olist.append(cnt)
            if not index: index = [cnt, cnt + 1, cnt + 2, cnt + 3]
            if ingredient[index[0]] == 1 and ingredient[index[1]] == 2 and ingredient[index[2]] == 3 and ingredient[index[3]] == 1:
                s, e = index[0], index[3]
                olist.pop()
                if not olist:
                    index, cnt = [], e
                else:
                    index = []
                    for i in range(olist.pop(), cnt): index.append(i)
                    while len(index) != 4: 
                        e += 1
                        index.append(e)
            else: index = []
        cnt += 1
        print(index, olist)
        
def solution(ingredient):
    from collections import deque
    igr, stk, flag, res = deque(ingredient), [], False, 0
    while igr:
        igrtmp = igr.popleft()
        if flag and igrtmp == 1 and stk[-1] == 3:
            if not igr: 
                res += 1
                break
            for _ in range(0, 3): stk.pop()
            for _ in range(0, len(stk)):
                tmpflag = False
                if not tmpflag and stk[-1] == 1: tmpflag = True
                elif tmpflag and stk[-1] != 1: break
                igr.appendleft(stk.pop())
            flag, stk, res = False, [], res + 1
            # print(stk, flag, igr)
            continue
        if flag and stk[-1] + 1 != igrtmp: flag = False
        if not flag and igrtmp == 1: flag = True
        stk.append(igrtmp)
        # print(stk, flag, igr)
    return res

def solution(ingredient):
    from collections import deque
    igr, stk, flag, res = deque(ingredient), deque(), False, 0
    igr.append(0)
    while igr:
        if len(stk) >= 4 and flag and stk[-1] == 1 and stk[-2] == 3 and stk[-3] == 2 and stk[-4] == 1:
            for _ in range(0, 4): stk.pop()
            while stk:
                if stk[0] == 1: break
                stk.popleft()
            for i in range(0, len(stk)):
                if flag and stk[i] != stk[i - 1] + 1: flag = False
                if not flag and stk[i] == 1: flag = True
            res = res + 1
        stk.append(igr.popleft())
        if stk[-1] != 1: flag = False
        print(stk)
        if flag and stk[-1] != stk[-2] + 1: flag = False
        if not flag and stk[-1] == 1: flag = True
    
    return res
            

print(solution( [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))

# 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1
# 2, 3, 2, 3, 1, 2, 3, 1
        
    
