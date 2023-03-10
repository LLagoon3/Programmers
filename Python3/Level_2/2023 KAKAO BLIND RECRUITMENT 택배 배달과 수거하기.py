#https://school.programmers.co.kr/learn/courses/30/lessons/150369?language=python3

def solution(cap, n, deliveries, pickups):
    res= 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        if pickups[i] == 0 and deliveries[i] == 0:
            cnt += 1
        else:
            break
    while 1:     
        deliveries, pickups = deliveries[:n - cnt], pickups[:n - cnt]
        n = n - cnt
        res = res + n
        if n == 0:
           break
        cnt = 0
        deli, pick, stop_cnt = cap, cap, False
        for i in range(n - 1, -1, -1):
            if deli > 0:
                if deli >= deliveries[i]:
                    deli = deli - deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] = deliveries[i] - deli
                    deli = 0
                    stop_cnt = True
            if pick > 0:
                if pick >= pickups[i]:
                    pick = pick - pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] = pickups[i] - pick
                    pick = 0
                    stop_cnt = True
            if pick == 0 and deli == 0 and (pickups[i] != 0 or deliveries[i] != 0):
                break
            if pickups[i] == 0 and deliveries[i] == 0 and not stop_cnt:
                cnt += 1
    return (res) * 2

def solution1(cap, n, deliveries, pickups):
        deli, pick = True, True

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(2, 7, [0, 0, 2, 0, 0, 0, 0], [0, 2, 0, 0, 2, 0, 0]))
print(solution(2, 2, [0, 0], [0, 4]))