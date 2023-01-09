#https://school.programmers.co.kr/learn/courses/30/lessons/150369?language=python3

def solution(cap, n, deliveries, pickups):
    res= 0

    while 1: 
        cnt = 0
        for j in range(n - 1, -1, -1):
            if deliveries[j] == pickups[j] == 0:
                cnt += 1
            else:
                break
        deliveries, pickups = deliveries[:n - cnt], pickups[:n - cnt]
        n = n - cnt
        res = res + n
        if n == 0:
           break

        deli, pick = cap, cap
        for i in range(n - 1, -1, -1):
            if deli > 0:
                if deli > deliveries[i]:
                    deli = deli - deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] = deliveries[i] - deli
                    deli = 0
            else:
                break
        for i in range(n - 1, -1, -1):
            if pick > 0:
                if pick > pickups[i]:
                    pick = pick - pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] = pickups[i] - pick
                    pick = 0
            else:
                break
            
    return (res) * 2

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))