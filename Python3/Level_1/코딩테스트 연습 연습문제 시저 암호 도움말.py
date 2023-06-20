def solution(s, n):
    res = ""
    for a in s:
       if ord(a) == 32:res += ' '
       elif 65 <= ord(a) <= 90: res += chr(((ord(a) - 65) % 25) + n + 65)
       elif 97 <= ord(a) <= 122: res += chr(((ord(a) - 97) % 25) + n + 97)
    return res
        
print(solution("a B z", 2))
# print(ord('Z')) #97 - 122 , 65 - 90