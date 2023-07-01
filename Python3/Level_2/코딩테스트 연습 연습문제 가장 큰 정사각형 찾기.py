def bfs(board, pos):
    area = 1
    for i in range(pos[1] + 1, len(board[0])):
        if board[pos[0]][i] == 0: break
        else: area += 1
    for y in range(pos[1], pos[1] + area):
        for x in range(pos[0] + 1, len(board)):
            if board[x][y] == 0 and area > x - pos[0]: 
                area = x - pos[0]
                break
    if area > len(board) -pos[0]: area = len(board) - pos[0]
    return area

def solution(board):
    area = 1
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if board[x][y] == 1:
                tmp = bfs(board, [x, y])
                if tmp > area: area = tmp
    return area ** 2

def solution(board):
    dp, res = [[0 for _ in range(0, len(board[0]) + 1)] for _ in range(0, len(board) + 1)], 0
    for x in range(1, len(board) + 1):
        for y in range(1, len(board[0]) + 1):
            if board[x - 1][y - 1] == 1:
                a, b, c = dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]
                dp[x][y] = min(a, b, c) + 1
                if dp[x][y] > res: res = dp[x][y]
    return res ** 2


t= [[0, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1]]
# t = [[1, 1, 0], [1, 0, 1]]
t = [[1, 1, 0, 1, 1, 1, 0], 
     [1, 1, 1, 1, 1, 1, 0], 
     [1, 0, 1, 1, 1, 1, 1], 
     [1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1]]
# t = [[0,0,0,1,1,1],
#      [0,0,0,1,1,1],
#      [1,1,1,1,1,1],
#      [1,1,1,1,1,1],
#      [1,1,1,1,1,1],
#      [1,1,1,1,1,1]]
t = [[1, 1], [0, 1]]
print(solution(t))

# print([[0 for i in range(0, 10)] for i in range(0, 10)])
