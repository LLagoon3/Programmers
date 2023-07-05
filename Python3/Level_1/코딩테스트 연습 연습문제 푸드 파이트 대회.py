def solution(food):
    res = ''
    for i in range(1, len(food)):
        res += str(i) * (food[i] // 2)
    return res + '0' + res[::-1]

print(solution([1, 3, 4, 6]))