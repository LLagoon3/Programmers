from collections import deque

def bfs(board, r, g):
    q, mv, visited = deque([r]), {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}, []
    while q:
        npos = q.popleft()
        if npos[:-1] in visited: continue
        else: visited.append(npos[:-1])
        for val in mv.values():
            tmppos, tmp = [npos[0], npos[1]], None
            while (0 <= tmppos[0] + val[0] < len(board)) and (0 <= tmppos[1] + val[1] < len(board[0])):
                tmppos = [tmppos[0] + val[0], tmppos[1] + val[1]]
                if board[tmppos[0]][tmppos[1]] == 'D': break
                tmp = tmppos
            if tmp == g: return npos[2] + 1
            elif tmp != None:
                tmp.append(npos[2] + 1)
                q.append(tmp)
    return -1
    
def solution(board):
    r, g, board = [0, 0, 0], [0, 0], list(map(list, board))
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 'R': r = [x, y, 0]
            elif board[x][y] == 'G': g = [x, y]
    return bfs(board, r, g)

print(solution([".D.R", "....", ".G..", "...D"]))