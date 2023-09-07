def solution(want, number, discount):
    from collections import deque, Counter
    res, q, length, index = 0, deque([0]), sum(number), dict()
    for i in range(0, length - 1): q.append(discount[i])
    for i, w in enumerate(want): index[w] = number[i]
    for i in range(length - 1, len(discount)):
        q.popleft()
        q.append(discount[i])
        # print(dict(Counter(q)))
        tmpindex, flag = dict(Counter(q)), True
        for key, val in index.items():
            if key in tmpindex.keys() and tmpindex[key] >= val:
                continue
            else:
                flag = False
                break
        if flag: res += 1
                
    return res
    
print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
