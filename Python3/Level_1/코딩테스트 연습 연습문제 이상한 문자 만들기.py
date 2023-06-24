def solution(s):
    res = ''
    for sn in s.split(' '):
        for i in range(0, len(sn)):
            if i % 2 == 0: res += sn[i].upper()
            else: res += sn[i].lower()
        res += ' '
    return res[:-1]

print(solution("try hello world"))
