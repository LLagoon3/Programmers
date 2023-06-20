arr1, arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
def solution(arr1, arr2):
    n, n_cnt, a, b = len(arr1[0]), 0, len(arr1), len(arr2[0])
    res = []
    for i in range(0, a):
        tmp = []
        for j in range(0, b):
            tmp.append(0)
        res.append(tmp)
    for aa in range(0, a):
        for nn in range(0, n):
            for bb in range(0, b):
                res[aa][bb] += arr1[aa][nn] * arr2[nn][bb]
    return res

print(solution(arr1, arr2))
    
    