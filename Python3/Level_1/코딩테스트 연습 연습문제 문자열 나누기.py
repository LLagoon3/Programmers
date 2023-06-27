def solution(s):
    res, stk = 0, [s[0]]
    for a in s[1:]:
        if stk == []: 
            res += 1
            stk.append(a)
        elif stk[-1] == a: stk.append(a)
        else: stk.pop()
    
    return res + (1 if not stk or len(set(stk)) == 1 else 2)

print(solution("aaaaaa"))