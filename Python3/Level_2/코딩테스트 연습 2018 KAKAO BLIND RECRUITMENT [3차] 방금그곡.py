m, musicinfos = "ABCDEFG", ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"]
# m, musicinfos = "C", ["13:00,13:01,WORLD,F"]

def caltime(st, et):
    st, et = (st.split(':')), (et.split(':'))
    sth, stm, eth, etm = int(st[0]), int(st[1]), int(et[0]), int(et[1])
    if sth > eth and eth == 0: eth = 24
    return (eth - sth) * 60 + (etm - stm)

def trans(p):
    index = {'C':'H', 'D':'I', 'F':'J', 'G':'K', 'A':'L', 'E': 'M'}
    def trans_(s):
        ptmp = []
        for i in s:
            if i == '#':ptmp.append(index[ptmp.pop()])
            else: ptmp.append(i)
        return (''.join(ptmp))
    p = trans_(list(p))
    return p

def solution(m, musicinfos):
    from collections import deque
    res_titie, res_time= '(None)', 0
    for music in musicinfos:
        st, et, title, p = music.split(',')
        tlen, p = caltime(st, et), trans(p)
        if tlen > len(p):
            for _ in range(0, (len(m) // len(p)) + 1):p += p
        else: p = p[:tlen]
        if m in p and tlen > res_time: res_titie, res_time = title, tlen
        print(tlen)
    
    return res_titie

def solution(m, musicinfos):
    from collections import deque
    res_titie, musicq = '(None)', list()
    m = trans(m)
    for music in musicinfos:
        st, et, title, p = music.split(',')
        tlen, p = caltime(st, et), trans(p)
        musicq.append([tlen, title, p])
    musicq.sort(key = lambda x : x[0])
    
    for music in musicq:
        tlen, title, p = music
        if tlen > len(p):
            for _ in range(0, (len(m) // len(p)) + 1):p += p
        else: p = p[:tlen]
        if m in p :
            res_titie = title
            break
    
    return res_titie

print(solution(m, musicinfos))
