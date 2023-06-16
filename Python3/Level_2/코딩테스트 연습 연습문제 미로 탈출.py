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

# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))

def test(A, p, r, x):
    q = int((p + r) / 2)
    print(A[q])
    if A[q] == x: return True
    elif p >= r: return False
    if test(A, p, q - 1, x): return True
    if test(A, q + 1, r, x): return True
    return False
    
print(test([0, 1, 2, 3], 0, 3, 5))