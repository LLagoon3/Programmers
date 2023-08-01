def solution(number, k):
    start, length, number, res = -1, len(number) - k, list(map(int, (list(number)))), ''
    for _ in range(0, length):
        m = 0
        print(start + 1, k)
        for i in range(start + 1, k + 1):
            if number[i] > m: m, start = number[i], i
            if number[i] == 9: break
        res += str(m)
        k += 1
    return res
        
print(solution("4177252841",	4))
