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
            

print(solution([1, 1, 2, 3, 1, 2, 3, 1]))

        
    
