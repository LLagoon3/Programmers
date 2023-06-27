
def dfs(maps, pos):
    mv, s, res, maps[pos[0]][pos[1]]= [(1, 0), (-1, 0), (0, 1), (0, -1)], [pos], int(maps[pos[0]][pos[1]]), 'X'
    while s:
        npos = s.pop()
        for d in mv:
            x, y = npos[0] + d[0], npos[1] + d[1]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] != 'X':
                s.append([x, y])
                maps[x][y], res = 'X', res + int(maps[x][y])
    return res    

def solution(maps):
    maps, res = list(map(list, maps)), []
    for x in range(0, len(maps)):
        for y in range(0, len(maps[0])):
            if maps[x][y] != 'X':
                res.append(dfs(maps, [x, y]))
    return sorted(res) if res else [-1]

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))