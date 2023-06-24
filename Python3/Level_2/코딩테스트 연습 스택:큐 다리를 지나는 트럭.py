bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]

def solution(bridge_length, weight, truck_weights):
    from collections import deque
    time = 0
    q = deque(truck_weights)
    while q:
        tmp, cnt = [], 0
        while q:
            qtmp = q.popleft()
            if sum(tmp) + qtmp <= weight and cnt < bridge_length:
                tmp.append(qtmp)
                cnt += 1
            else: 
                q.appendleft(qtmp)
                break
        print(tmp, bridge_length + len(tmp) - 1)
        time += bridge_length + len(tmp) - 1
    return time + 1

def solution(bridge_length, weight, truck_weights):
    from collections import deque
    truck_weights, bridge, time, tcnt, bridgesum = deque(truck_weights), deque([0] * bridge_length), 0, 0, 0
    while truck_weights:
        tmp = bridge.popleft()
        if tmp != 0:
            tcnt -= 1
            bridgesum -= tmp
        time += 1
        tw = truck_weights.popleft()
        if tcnt < bridge_length and bridgesum + tw <= weight:
            bridge.append(tw)
            bridgesum += tw
            tcnt += 1
        else:
            truck_weights.appendleft(tw)
            bridge.append(0)
        print(bridge)
      
    return time + bridge_length
        

print(solution(bridge_length, weight, truck_weights))
        