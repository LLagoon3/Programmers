def solution(numbers):
    from itertools import permutations, combinations
    numbers = sorted(list(numbers))
    maxn = int(''.join(numbers[::-1]))
    index = [True for i in range(0, maxn + 1)]
    index[0], index[1] = False, False
    for i in range(2, maxn + 1):
        if index[i]:
            for j in range(2 * i, maxn + 1, i):
                index[j] = False
    numlist, res = list(), 0
    for i in range(1, len(numbers) + 1):
        for num in list(permutations(numbers, i)):
            num = int(''.join(num))
            if num not in numlist and index[num]:
                res += 1
                numlist.append(num)
    return res
        
print(solution("011"))