#two-dimensional
def modmap(t, x, y):
    if x >= y: ssx1, ssy1 = x - y, 0
    else: ssx1, ssy1 = 0, y - x
    ssx2, ssy2 = 0, x + y
    for tmp in range(0, len(t)):
        if t[tmp][y] != -1: t[tmp][y] = 1
        if t[x][tmp] != -1: t[x][tmp] = 1
        if ssx1 + tmp < len(t) and ssy1 + tmp < len(t):
            if t[ssx1 + tmp][ssy1 + tmp] != -1 :t[ssx1 + tmp][ssy1 + tmp] = 1
        if 0 <= ssy2 - tmp < len(t): 
            if t[ssx2 + tmp][ssy2 - tmp] != -1: t[ssx2 + tmp][ssy2 - tmp] = 1
    t[x][y] = -1
    return t

def chkmap(stack, t):
    for i in range(0, len(t)):
        for j in range(0, len(t)):
            if t[i][j] == 0:stack.append([i, j])
    return stack

from copy import deepcopy
def dfs(n, t, stack = [], qcnt = 0, visit = []):
    while stack:
        tmpt, tmpstack= deepcopy(t), []
        tmp = stack.pop()
        if qcnt == n - 1:
            t[tmp[0]][tmp[1]] = -1
            if t not in visit: visit.append(t)
            return visit
        tmpt = modmap(tmpt, tmp[0], tmp[1])
        tmpstack = chkmap(tmpstack, tmpt)
        if tmpstack: visit = dfs(n, tmpt, tmpstack, qcnt + 1)
    return visit
        
def solution(n):
    t = [[0 for i in range(0, n)] for j in range(0, n)]
    print((dfs(n, t, chkmap([], t))))


#one-dimensional
from copy import deepcopy
def dfs(board, k = 0, res = 0):
    if k == len(board):
        if -1 not in board: return res + 1
        else: return res
    stack= {i for i in range(0, len(board))}
    for x in range(0, k):
        y = board[x]
        stack.discard(y)
        stack.discard(y + k - x)
        stack.discard(y - k + x)
    while stack:
        tmp = deepcopy(board)
        tmp[k] = stack.pop()
        res = dfs(tmp, k + 1, res)
    return res
    
def solution(n):
    board = [-1 for i in range(0, n)]
    return dfs(board)

print(solution(4))