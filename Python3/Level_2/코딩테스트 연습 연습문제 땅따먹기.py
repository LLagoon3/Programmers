land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    maxland = [land[0]]
    for i in range(1, len(land)):
        tmpland = []
        for j in range(0, len(land[0])):
            tmp = maxland[-1].copy()
            tmp[j] = -1
            tmpland.append(land[i][j] + max(tmp))
        maxland.append(tmpland)
    
    return max(maxland[-1])

print(solution(land))