def solution(k, dungeons):
    from itertools import permutations
    t, res = [i for i in range(0, len(dungeons))], 0
    for i in list(permutations(t, len(t))):
        tmpres, tmpk = 0, k
        for di in i:
            if tmpk >= dungeons[di][0]:
                tmpres += 1
                tmpk -= dungeons[di][1]
            else: break
        if tmpres == len(dungeons): return tmpres
        elif tmpres > res: res = tmpres
    return res
    
print(solution(80, [[80,20],[50,40],[30,10]]))