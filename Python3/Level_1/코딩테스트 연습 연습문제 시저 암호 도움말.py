def solution(s, n):
    res = ""
    for a in s:
        asc = ord(a)
        if asc == 32: res += ' '
        elif asc <= 90: res += chr(((asc - 65 + n) % 26) + 65)
        elif asc >= 97: res += chr(((asc - 97 + n) % 26) + 97)
    return res
        
print(solution("a B z", 26))
# print(ord('Z')) #97 - 122 , 65 - 90