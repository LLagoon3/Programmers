s = "Zbcdefg"

def solution(s):
    s = sorted(s)
    res = ""
    while s: res += s.pop()
    return res

print(solution(s)) 