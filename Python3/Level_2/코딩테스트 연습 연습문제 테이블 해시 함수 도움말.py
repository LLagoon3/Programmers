data = [[2,2,6],[1,5,10],[4,2,9],[1, 5, 10], [3,8,3]]

def solution(data, col, row_begin, row_end):
    from collections import deque
    db, tmp = deque(), [0] * len(data[0])
    for i in range(0, len(data)):
        index, maxcol, maxkey = [], 0, 0
        for j, d in enumerate(data):
            if d[col - 1] > maxcol:index, maxcol, maxkey = [j], d[col - 1], d[0]
            elif d[col - 1] == maxcol:
                if d[0] < maxkey: index, maxcol, maxkey = [j], d[col - 1], d[0]
                elif d[0] == maxkey:
                    index.append(j)
                    maxcol, maxkey = d[col - 1], d[0]
        for j in index: 
            db.appendleft(data[j])
            data[j] = tmp
        if len(db) >= len(data) - row_begin + 1: break
    
    si = 0
    for i in range(0, row_end - row_begin + 1):
        tsi = 0
        for j in range(0, len(db[0])): tsi += db[i][j] % (i + row_begin)
        si = si ^ tsi
    print(db)
    return si
print(solution(data, 2, 2, 4))




