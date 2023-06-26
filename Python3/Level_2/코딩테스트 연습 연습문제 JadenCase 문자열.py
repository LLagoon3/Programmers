def solution(s):
    res = []
    for ss in s.split(' '):
        if ss == '': res.append(ss)
        elif ss[0].isnumeric(): res.append(ss.lower())
        else: res.append(ss[0].upper() + ss[1:].lower())
    return ' '.join(res)
    
print((solution(" 1ppppppp")))
