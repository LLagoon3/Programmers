
input = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# input = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

mv = [[-1, 0], [1, 0], [0, -1], [0, 1]] #UDLW

def dfs(maps, pos, visited):
    res, cnt = [100001], 0
    if pos == [len(maps) - 1, len(maps[0]) - 1]:
        return len(visited)
    for dir in mv:
        n_pos = [pos[0] + dir[0], pos[1] + dir[1]]
        if n_pos[0] >= 0 and n_pos[1] >= 0 and n_pos[0] < len(maps) and n_pos[1] < len(maps[0]) and maps[n_pos[0]][n_pos[1]] != 0 and n_pos not in visited:
            visited.append(n_pos)
            cnt += 1
            r = dfs(maps, n_pos, visited)
            visited.pop()
            res.append(r)
    return min(res)

def bfs(maps, pos):
    from collections import deque
    q = deque([pos + [1]])
    max_x, max_y = len(maps) - 1, len(maps[0]) - 1
    if (maps[max_x - 1][max_y] == 0 and maps[max_x][max_y - 1] == 0): return -1
    while q:
        p = q.popleft()
        if p[0] == max_x and p[1] ==  max_y: return p[2]
        for d in mv:
            x, y = p[0] + d[0], p[1] + d[1]
            if x >= 0 and y >= 0 and x <= max_x and y <= max_y and maps[x][y] != 0:
                if maps[p[0]][p[1]] == 1: maps[p[0]][p[1]] = 0
                q.append([x, y, p[2] + 1])
    return -1
         
####################################################################################

def bfs(maps):
    mv = [[-1, 0], [1, 0], [0, -1], [0, 1]] #UDLW
    from collections import deque
    q = deque([[0, 0, 0]])
    while q:
        pos = q.popleft()
        for d in mv:
            x, y = pos[0] + d[0], pos[1] + d[1]
            if x == len(maps) - 1 and y == len(maps[0]) - 1: return pos[2] + 2
            elif 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] != 0:
                maps[x][y] = 0
                q.append([x, y, pos[2] + 1])
                print(x, y)
    return -1
            

def solution(maps):
    pos = [0, 0]
    # answer = dfs(maps, pos, [pos])
    answer = bfs(maps)
    return answer

print(solution(input))