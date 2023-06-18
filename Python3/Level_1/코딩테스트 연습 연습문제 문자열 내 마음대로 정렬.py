
def solution(st, n):
    res = [st[0]]
    for w in st[1:]:
        mod = False
        for index, r in enumerate(res):
            if w[n] < r[n]: 
                res.insert(index, w)
                mod = True
                break
            elif w[n] == r[n]:
                if w < r: 
                    res.insert(index, w)
                    mod = True
                    break
                elif w == r: 
                    res.insert(index + 1, w)
                    mod = True
                    break
        if not mod: res.append(w)
    return res

print(solution(["abce", "cdxa", "abcd", "aeoz"], 0))

#####
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])