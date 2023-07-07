def meetpoint(exp1, exp2):
    if (exp1[1] == 0 and exp2[1] == 0) or (exp1[0] == 0 and exp2[0] == 0): return False
    if (exp1[1]*exp2[0] - exp2[1]*exp1[0]) == 0: x = exp1[3]
    else: x = (exp2[1]*exp1[2] - exp1[1]*exp2[2]) / (exp1[1]*exp2[0] - exp2[1]*exp1[0])
    if x % 1 == 0: x = int(x)
    else: return False
    
    if exp1[1] == 0: y = -(exp2[0]*x + exp2[2]) / exp2[1]
    else: y = -(exp1[0]*x + exp1[2]) / exp1[1]
    if y % 1 == 0: return [x, int(y)]
    else: return False
    
def meetpoint(exp1, exp2):
    if (exp1[0] * exp2[1]) - (exp1[1] * exp2[0]) == 0: return False
    x = (exp2[1]*exp1[2] - exp1[1]*exp2[2]) / (exp1[1]*exp2[0] - exp2[1]*exp1[0])
    if x % 1 == 0: x = int(x)
    else: return False
    
    if exp1[1] == 0: y = -(exp2[0]*x + exp2[2]) / exp2[1]
    else: y = -(exp1[0]*x + exp1[2]) / exp1[1]
    if y % 1 == 0: return [x, int(y)]
    else: return False
    
def mkstar(minx, miny, maxx, maxy, point):
    star = [['.' for _ in range(0, maxx - minx + 1)] for _ in range(0, maxy - miny + 1)]
    for p in point:
        x, y = p[1] - miny, p[0] - minx
        star[x][y] = '*'
        # print(p, [x, y])
    res = list()
    while star: res.append(''.join(star.pop()))
    return res

def solution(line):
    minx, miny, maxx, maxy, point = 9223372036854775807, 9223372036854775807, -9223372036854775807, -9223372036854775807, list()
    for i in range(0, len(line)):
        for j in range(i + 1, len(line)):
            tmp = meetpoint(line[i], line[j])
            if tmp: 
                point.append(tmp)
                minx, miny, maxx, maxy = min(tmp[0], minx), min(tmp[1], miny), max(tmp[0], maxx), max(tmp[1], maxy)
    return mkstar(minx, miny, maxx, maxy, point)

c1 = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
c2 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
c3 = [[1, -1, 0], [2, -1, 0]]
c4 = [[0, 1, 1], [1, 0, 3], [1, 0, 1], [-1, 1, -2]]
print(solution(c4))