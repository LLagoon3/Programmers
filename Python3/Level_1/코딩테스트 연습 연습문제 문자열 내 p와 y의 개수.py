s = "PoooyY"

def solution(s):
    res = 0
    for a in s:
        if a == 'p' or a == 'P': res += 1
        elif a == 'y' or a == 'Y': res -= 1
    if res == 0: return True
    else: return False

print(solution(s))