def chks(word, cnt, s):
    index, flag = ['A', 'E', 'I', 'O', 'U'], False
    cnt += 1
    print(s, cnt)
    if s == word: return cnt, True
    elif len(s) == 5: return cnt, flag
    
    for i in index:
        cnt, flag = chks(word, cnt, s + i)
        if flag: return cnt, flag
        
    return cnt, flag
    
    
def solution(word):
    cnt, s = 0, ''
    res, tmp = chks(word, cnt, s)
    return res - 1
    
print(solution('I'))