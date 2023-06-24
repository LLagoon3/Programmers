park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]	

def solution(park, routes):
    flag = False
    d = {'E': [0, 1],
         'S': [1, 0],
         'W': [0, -1], 
         'N': [-1, 0]}
    for x in range(0, len(park)):
        if flag: break
        for y in range(0, len(park[0])):
            if park[x][y] == 'S':
                sx, sy, flag = x, y, True
                break
    def chk(x, y, op, n):
        for i in range(0, n):
            x, y = x + d[op][0], y + d[op][1]
            if not(0 <= x < len(park) and 0 <= y < len(park[0]) and (park[x][y] == 'O' or park[x][y] == 'S')):
                return False
        return True
    
    for ir in routes:
        op, n = ir.split(' ')
        n = int(n)
        if chk(sx, sy, op, n):
            sx, sy = sx + d[op][0] * n, sy + d[op][1] * n
    
    return [sx, sy]

print(solution(park, routes))
        