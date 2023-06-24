def solution(weights):
    save, cnt= dict(), 0
    for i in range(0, len(weights)):
        for j in range(i + 1, len(weights)):
            miw, maw = min(weights[i], weights[j]), max(weights[i], weights[j])
            if maw > miw *2: continue
            index = "{0}-{1}".format(miw, maw)
            if index in save: 
                cnt += 1
                continue
            elif weights[i] == weights[j]:
                save[index] = True
                cnt += 1
                continue
            tmp = [miw * 2, miw * 3 / 2, miw * 4 / 3]
            print(miw, maw, tmp)
            if maw in tmp: 
                save[index] = True
                cnt += 1
                continue
    return cnt

def solution(weights):
    from collections import Counter, deque
    cnt = 0
    w = dict(Counter(weights))
    k = sorted(list(w.keys()))
    while k:
        key = k.pop()
        val = w[key]
        cnt += (val * (val - 1)) // 2
        for i in k:
            if key in [i * 2, i * 3 / 2, i * 4 / 3]: 
                cnt += w[i] * val
    return cnt

print(solution([100,180,360,100,270]))
print(solution([100,100,100,100,100]))
print(solution([2, 2, 1, 1, 1]))
