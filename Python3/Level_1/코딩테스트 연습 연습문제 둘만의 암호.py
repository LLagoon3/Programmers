print(ord('a'), ord('z'))

t = 'az'
print(list(map(ord, t)))

def solution(s, skip, index):
    s, skip = list(map(ord, s)), list(map(ord, skip))
    for a in range(0, len(s)):
        i = index
        while i > 0:
            s[a] += 1
            if s[a] > 122: s[a] = s[a] - 122 + 96
            if s[a] in skip: continue
            i -= 1
    return ''.join(list(map(chr, s)))
    
print(solution("zz", "wbqd", 5))