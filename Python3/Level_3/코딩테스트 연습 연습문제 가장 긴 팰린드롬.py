def solution(s):
    for l in range(len(s), 0, -1):
        for start in range(0, len(s) - l + 1):
            tmps = s[start:start + l]
            if tmps == tmps[::-1]: return l
            
print(solution("a"))