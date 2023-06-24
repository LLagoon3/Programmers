def solution(numbers):
    from collections import deque
    res, ma = deque(), numbers[-1]
    res.append(-1)
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] > numbers[i + 1]:
            if numbers[i] >= ma:
                res.appendleft(-1)
                ma = numbers[i]
                continue
            flag = False
            for j in range(i + 2, len(numbers)):
                if numbers[j] > numbers[i]: 
                    res.appendleft(numbers[j])
                    flag = True
                    break
                elif numbers[j] == numbers[i]:
                    res.appendleft(res[j - len(numbers)])
                    flag = True
                    break
            if not flag: res.appendleft(-1)
        elif numbers[i] == numbers[i + 1]: res.appendleft(res[0])
        else: res.appendleft(numbers[i + 1])
    return list(res)

print(solution([5, 3, 5, 3, 5, 3, 6]))

        