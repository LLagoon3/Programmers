def solution(sequence, k):
    from collections import deque
    res, tmp, sum = list(), deque(), 0
    for i in range(0, len(sequence)):
        tmp.append(sequence[i])
        sum += sequence[i]
        if sum == k: res.append([i - len(tmp) + 1, i])
        elif sum > k:
            while 1:
                sum -= tmp.popleft()
                if sum < k: break
                elif sum == k:
                    res.append([i - len(tmp) + 1, i])
    minval, minpos = 1000001, list()
    for i in range(0, len(res)):
        tmp = res.pop()
        if tmp[1] - tmp[0] <= minval: minval, minpos = tmp[1] - tmp[0], tmp
    return minpos
    
print(solution([1, 1, 1, 2, 3, 4, 5], 7))
    