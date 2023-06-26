k, t = ["ABACD", "BCEFD"], ["ABCD","AABB"]

def solution(keymap, targets):
    index, maxlen, res = dict(), max(list(map(len, keymap))), []
    def cnt(a):
        if a in index.keys(): return index[a]
        for i in range(0, maxlen):
            for map in keymap:
                if len(map) > i and map[i] == a:
                    index[a] = i + 1
                    return i + 1
        index[a] = -1
        return -1
    for t in targets:
        tmp = 0
        for a in t:
            if cnt(a) == -1:
                tmp = -1
                break
            tmp += cnt(a)
        res.append(tmp)
    return res

print(solution(k, t))


def solution(s):
    cnt = 0
    for k in range(0, len(s)):
        for i in range(k + 1, len(s)):
            k_, i_ = k, i
            if s[k_] == s[i_]:
                tmp = s[k_]
                while k_ < i_:
                    k_ += 1
                    i_ -= 1
                    if s[k_] != tmp: 
                        cnt += i - k_
                        break
                    elif s[i_] != tmp: 
                        cnt += i_ - k
                        break  
            else: 
                cnt += i - k
    return cnt

def solution(s):
    index, res = [0] * len(s), 0
    for start in range(0, len(s)):
        for end in range(start + 1, len(s)):
            if s[start] == s[end]:
                # if len(set(s[start:end + 1])) == 1: 
                #     res += 0
                #     continue
                tmpcnt, indexstart, indexend, tmps = 0, 0, 0, s[start]
                if index[start] != 0: indexstart = index[start]
                if index[end] != 0: indexend = index[end]
                if indexend > 0 or indexstart < 0: continue
                while tmpcnt <= ((end - start) // 2) + 1:
                    tmpcnt += 1
                    if indexstart == 0 and index[start + tmpcnt] and s[start + tmpcnt] == tmps != 0: 
                        indexstart = index[start + tmpcnt] + tmpcnt
                        index[start] = indexstart
                    elif indexstart == 0 and s[start + tmpcnt] != tmps:
                        indexstart, index[start] = tmpcnt, tmpcnt
                    if indexend == 0 and index[end - tmpcnt] and s[end - tmpcnt] == tmps != 0:
                        indexend = index[end - tmpcnt] - tmpcnt
                        index[end] = indexend
                    elif indexend == 0 and s[end - tmpcnt] != tmps:
                        indexend, index[end] = tmpcnt, -tmpcnt
                    if indexstart != 0 and indexend != 0:
                        print('start : ', start, ' end : ', end, ' indexstart : ', indexstart, ' indexend : ', indexend, ' index : ', index, ' cnt : ', tmpcnt)
                        res += max(indexstart, -indexend)
                        
                        break
            else: 
                res += end - start
                print('start : ', start, ' end : ', end)
    print(index)
    return res

print(solution("abaab"))