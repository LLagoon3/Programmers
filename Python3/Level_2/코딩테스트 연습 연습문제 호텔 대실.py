def solution(book_time):
    res, time = [], []
    for t in book_time:
        sth, stm, eth, etm = int(t[0].split(':')[0]), int(t[0].split(':')[1]), int(t[1].split(':')[0]), int(t[1].split(':')[1])
        time.append([sth * 60 + stm, eth * 60 + etm + 10]) 
    time.sort(reverse = True, key = lambda x : x[1])
    res.append(time.pop()[1])
    while time:
        t = time.pop()
        mi = [-1, -1]
        for index, bt in enumerate(res):
            if t[0] >= bt and bt > mi[1] : mi = [index, bt]
        if mi[0] == -1: res.append(t[1])
        else: res[mi[0]] = t[1]
    return len(res)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
        