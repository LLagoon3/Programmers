m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

def cal(m, n, board):
    res, dir = [], [[1, 0], [0, 1], [1, 1]]
    for x in range(0, m):
        for y in range(0, n):
            tmp, a = [], board[x][y]
            if a == '*': continue
            for d in dir:
                xx, yy= x + d[0], y + d[1]
                if 0 <= xx < m and 0 <= yy < n:
                    if board[xx][yy] != a: break
                    tmp.append([xx, yy])
            tmp.append([x, y])
            if len(tmp) == 4:
                for i in tmp: 
                    if i not in res: res.append(i)
    return res

def mkboard(m, n, board):
    for y in range(0, n):
        for x in range(0, m):
            if board[x][y] == '*':
                for i in range(x, 0, -1): board[i][y] = board[i - 1][y]
                board[0][y] = '*'
    return board

def solution(m, n, board):
    for index, i in enumerate(board): board[index] = list(i)
    res, tmp = [], [-1]
    while tmp:
        tmp = cal(m, n, board)
        for i in tmp: 
            res.append(i)
            board[i[0]][i[1]] = '*'
        board = mkboard(m, n, board)
    return len(res)
    
print(solution(m, n, board))
            
            
                
            
            