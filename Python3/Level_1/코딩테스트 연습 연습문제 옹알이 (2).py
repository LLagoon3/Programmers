def solution(babbling):
    res = 0
    for b in babbling:
        index = ["aya", "ye", "woo", "ma"]
        for i in range(0, 4):
            while 1:
                if index[i] in b:
                    b = b.replace(index[i], '*', 1)
                else: break
        flag = True
        for b_ in b:
            if b_ != '*': 
                flag = False
                break
        if flag: 
            res += 1
    return res

def solution(babbling):
    res = 0
    from collections import deque
    for b in babbling:
        b, tmp = deque(b), ''
        while b:
            if len(b) > 1 and (b[0] + b[1] != tmp) and (b[0] + b[1] in ['ye', 'ma']):
                tmp = b.popleft() + b.popleft()
            elif len(b) > 2 and (b[0] + b[1] + b[2] != tmp) and (b[0] + b[1] + b[2] in ['aya', 'woo']):
                tmp = b.popleft() + b.popleft() + b.popleft()
            else: break
        if not b: res += 1
    return res

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(solution(["ayayeayayeaya"]))
