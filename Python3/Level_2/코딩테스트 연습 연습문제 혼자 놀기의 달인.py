def solution(cards):
    from copy import deepcopy
    cards, res = [0] + cards, list()
    for _ in range(0, 2):
        tmp = [[] for _ in range(0, len(cards))]
        for i in range(1, len(cards)):
            tmpc, index = deepcopy(cards), i
            if tmpc[i] == 0: continue
            for _ in range(1, len(cards)):
                if tmpc[index] == 0: break
                tmp[i].append(tmpc[index])
                tmpi = index
                index = tmpc[index]
                tmpc[tmpi] = 0
        tmp = max(tmp, key = lambda x: len(x) if x != [] else -1)
        # print(tmp)
        res.append(len(tmp))
        for i in tmp: cards[i] = 0
        if sum(cards) == 0: break
    if len(res) == 1: return 0  
    return res[0] * res[1]

print(solution([8,6,3,7,2,5,1,4]))
        
            
        