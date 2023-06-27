n, k, e = 7, 3, [4, 2, 4, 5, 3, 3, 1]
# n, k, e = 2, 4, [3, 4, 7, 10, 10]

#### Using Binary Tree ####
def solution(n, k, enemy):
    bt = [[-1, -1] for i in range(0, ((2 ** (len(enemy) + 1)) - 1))]
    bt[0] = [n, k]
    print((bt))
    node = 0
    for h in range(0, len(enemy)):
        flag = 0
        for index in range(0, 2 ** h):
            l, r = node * 2 + 1, node * 2 + 2
            bt[l] = [bt[node][0], bt[node][1] - 1]
            bt[r] = [bt[node][0] - enemy[h], bt[node][1]]
            if bt[l][0] <= 0 or bt[l][1] <= 0: flag += 1
            if bt[r][0] <= 0 or bt[r][1] <= 0: flag += 1
            node += 1
        print(bt)
        if flag == 2 ** (h + 1): return h + 1
    return len(enemy)

#### Using Leaf Node ####
def solution(n, k, enemy):
    result, cnt = [[n, k]], 0
    for i in range(0, len(enemy)):
        tmp = []
        for r in result:
            if r[1] - 1 >= 0: tmp.append([r[0], r[1] - 1])
            if r[0] - enemy[i] >= 0: tmp.append([r[0] - enemy[i], r[1]])
        cnt += 1
        result = tmp
        if not result: return cnt - 1
    return len(enemy)

#### O(n) with MaxHeap ####
def solution(n, k, enemy):
    from heapq import heappush, heappop
    elist = []
    for round, e in enumerate(enemy):
        print(round, n, k)
        heappush(elist, (-e, e))
        n -= e
        if n < 0 and k > 0:
            n += heappop(elist)[1]
            k -= 1
        elif n < 0 and k <= 0:
            print(round, n, k)
            return round
    return len(enemy)
print(solution(n, k, e))
