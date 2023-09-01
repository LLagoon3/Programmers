# 가위(0), 바위(1), 보(2)
# 두 개의 입력일 때 (0, 1) 중 누가 이길지, 비기면 -1

def solution(a, b):
    index = [1, 2, 3]
    if (a - 1) % 3 == b: return 0
    elif (a + 1) % 3 == b: return 1
    return -1

# print(solution(2, 0)) 



#### 프로그래머스 스킬체크 lv1

def solution(n):
    res = 1
    for i in range(2, n + 1):
        if n % i == 0: res += i
    return res

# print(solution(0))



#### 프로그래머스 스킬체크 lv2

def solution(msg):
    dic, ch, res = dict(), 65, []
    for i in range(1, 27):
        dic[chr(ch)] = i
        ch += 1
    while msg:
        mpos = 1
        while mpos <= len(msg):
            if msg[:mpos] in dic.keys():
                mpos += 1
            else: break
        if mpos > 1: mpos -= 1
        tmpmsg = msg[:mpos]
        msg = msg[mpos:]
        res.append(dic[tmpmsg])
        if msg != '' and (tmpmsg + msg[0] not in dic.keys()):
            dic[tmpmsg + msg[0]] = len(dic.keys()) + 1
    print(dic)
    return res
    
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))


#### 프로그래머스 스킬체크 lv2

def solution(numbers):
    from itertools import permutations
    res = []
    for i in range(1, len(numbers) + 1):
        p = list(permutations(list(map(int, list(numbers))), i))
        for k in p:
            tmp = ''
            for j in k: tmp += str(j)
            tmp, flag = int(tmp), True
            if tmp not in res:
                for j in range(2, int(tmp ** 0.5) + 1):
                    if tmp % j == 0:
                        flag = False
                        break
                if flag: res.append(tmp)
    l = len(res)
    print(res)
    if 1 in res: l -= 1
    if 0 in res: l -= 1
    return l
# print(solution("017"))



###

