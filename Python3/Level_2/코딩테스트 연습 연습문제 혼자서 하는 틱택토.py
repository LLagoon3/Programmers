#https://school.programmers.co.kr/learn/courses/30/lessons/160585

def solution(board):
    o_cnt, x_cnt = 0, 0
    o_line_cnt, x_line_cnt = 0, 0
    for row in board:
        o_cnt = o_cnt + row.count('O')
        x_cnt = x_cnt + row.count('X')
    if not (o_cnt == x_cnt or o_cnt == x_cnt + 1):
        return 0
    def chk(st):
        nonlocal o_line_cnt
        nonlocal x_line_cnt
        if st == 'O':o_line_cnt += 1
        elif st == 'X':x_line_cnt += 1
    
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2]:
            chk(board[i][0])
        if board[0][i] == board[1][i] == board[2][i]:
            chk(board[0][i])
    if board[0][0] == board[1][1] == board[2][2]:
        chk(board[1][1])
    if board[0][2] == board[1][1] == board[2][0]:
        chk(board[1][1])
    if o_cnt + x_cnt != 9 and o_line_cnt + x_line_cnt > 1:
        return 0
    if o_cnt + x_cnt != 0 and o_cnt > x_cnt and x_line_cnt >= 1:
        return 0
    if o_cnt == x_cnt and o_line_cnt >= 1:
        return 0
    if o_cnt + x_cnt == 9 and o_line_cnt == x_line_cnt ==  1:
        return 0
    return 1

print(solution(["XXX", "XOO", "OOO"]))

