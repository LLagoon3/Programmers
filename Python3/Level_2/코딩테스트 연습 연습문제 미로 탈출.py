from collections import deque

def chkPosition(_map, map_width, pos):
    res, pos_info = [], ['u', 'l', 'r', 'd']
    if pos < map_width: pos_info.remove('u')
    if pos % map_width == 0: pos_info.remove('l')
    if pos % map_width == map_width - 1: pos_info.remove('r')
    if pos >= map_width*map_width - map_width: pos_info.remove('d')
    
    if 'u' in pos_info: res.append(pos - map_width)
    if 'l' in pos_info: res.append(pos - 1)
    if 'r' in pos_info: res.append(pos + 1)
    if 'd' in pos_info: res.append(pos + map_width)
    tmp = pos
    for pos in res:
        if _map[pos] == 'X': res.remove(pos)
    return res
    
def bfs(graph, target, root = 0):
    queue = deque()
    visited = [root]
    res = 0
    for i in graph[root]:
        queue.append(i)
    while 1:
        pos = queue.popleft()
        if pos not in visited:
            visited.append(pos)
            for i in graph[pos]:
                queue.append(i)
            print(pos, "\t", end= '')
            res += 1
            if pos == target:
                print("\n")
                return res
        
def dfs(graph, target, root, cnt, visited = []):
    tmp = []
    print(root, "\t", end='')
    visited.append(root)
    cnt += 1
    for i in graph[root]:
        if i == target:
            return len(visited)
        if i not in visited: tmp.append((dfs(graph, target, i, cnt, visited)))

    res = 100000
    if tmp == []: return -1
    else: 
        for i in tmp:
            if i != -1 and i < res:res = tmp
        return res
        
    
# 0  1  2  3  4
# 5  6  7  8  9
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24   

def solution(maps):
    answer = 0
    _map = []
    map_width = len(maps)
    graph = {}
    start , labber, end, cnt = 0, 0, 0, 0
    for row in maps:
        for col in range(0, len(row)):
            _map.append(row[col])
            if row[col] == 'S':
                start = cnt
            elif row[col] == 'L':
                labber = cnt
            elif row[col] == 'E':
                end = cnt
            cnt += 1
    
    for i in range(0, len(_map)):
        if not _map[i] == 'X':
            tmp = chkPosition(_map, map_width, i)
            graph[i] = tmp
    
    print("\n", dfs(graph, end, labber, 0))
    # answer += bfs(graph, labber, start)
    # answer += bfs(graph, end, labber)
    
    return answer

def bfs(maps, pos, target):
    from collections import deque
    q, index = deque([[pos[0], pos[1], '', 0]]), {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}
    d = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1)}
    while q:
        pos = q.popleft()
        if pos[0] == target[0] and pos[1] == target[1]: return pos[3]
        for k, v in d.items():
            if k == pos[2]: continue
            x, y = pos[0] + v[0], pos[1] + v[1]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] != 'X':##
                q.append([x, y, index[k], pos[3] + 1])
    return 0

def bfs(maps, vmaps, pos, target):
    from collections import deque
    q = deque([[pos[0], pos[1], 0, '']])
    d = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1)}
    if vmaps[target[0]][target[1]] and vmaps[pos[0]][pos[1]]: 
        t, p = vmaps[target[0]][target[1]], vmaps[pos[0]][pos[1]]
        print(t, p)
        for i in range(0, min(len(t), len(p))):
            if t[i] != p[i]: return len(t) + len(p) - (2 * i)
        return len(t) + len(p) - (2 * min(len(t), len(p)))
    while q:
        pos = q.popleft()
        if pos[0] == target[0] and pos[1] == target[1]: return pos[2]
        for k, v in d.items():
            x, y = pos[0] + v[0], pos[1] + v[1]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] != 'X' and vmaps[x][y] == '':##
                q.append([x, y, pos[2] + 1, pos[3] + k])
                vmaps[x][y] = pos[3] + k
    return 0

def solution(maps):
    info = {'S': None, 'E': None, 'L': None}
    vmaps = [['' for _ in range(0, len(maps[0]))] for _ in range(0, len(maps))]    
    for x in range(0, len(maps)):
        for y in range(0, len(maps[0])):
            if maps[x][y] in ['S', 'E', 'L']: info[maps[x][y]] = [x, y]
    path1 = bfs(maps, vmaps, info['S'], info['L'])
    print(vmaps)
    path2 = bfs(maps, vmaps, info['L'], info['E'])
    print(path1, path2)
    if path1 != 0 and path2 != 0: return path1 + path2
    else: return -1

def bfs(maps, info):
    from collections import deque
    q = deque([[info['S'][0], info['S'][1], 0, 0]])
    d = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1)}
    path1, path2, visited1, visited2 = 0, 0, [[info['S'][0], info['S'][1]]], [[info['L'][0], info['L'][1]]]
    while q:
        pos = q.popleft()
        if not pos: continue
        elif pos[0] == info['E'][0] and pos[1] == info['E'][1]:
            if pos[3] != 0:
                path1 , path2 = pos[2], pos[3] - 1
                print(path1, path2)
        for k, v in d.items():
            x, y = pos[0] + v[0], pos[1] + v[1]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] != 'X':
                if pos[3] == 0 and [x, y] not in visited1:
                    if maps[x][y] == 'L': 
                        q.append([x, y, pos[2] + 1, 1])
                        visited2.append([x, y])
                    else: 
                        q.append([x, y, pos[2] + 1, 0])
                        visited1.append([x, y])
                elif pos[3] != 0 and [x, y] not in visited2:
                    q.append([x, y, pos[2], pos[3] + 1])
                    visited2.append([x, y])
        # print(q)
    if path1 == 0 or path2 == 0:
        return -1
    return path1 + path2

def solution(maps):
    info = {'S': None, 'E': None, 'L': None}
    vmaps = [['' for _ in range(0, len(maps[0]))] for _ in range(0, len(maps))]    
    for x in range(0, len(maps)):
        for y in range(0, len(maps[0])):
            if maps[x][y] in ['S', 'E', 'L']: info[maps[x][y]] = [x, y]
    return bfs(maps, info)
    


print(solution(["SOOOL",
                "XXXXO",
                "OOOOO",
                "OXXXX",
                "OOOOE"]))
# print(solution(["SOOOE",
#                 "XOXXO",
#                 "OOOOO",
#                 "XXOXO",
#                 "OOOLO"]))

