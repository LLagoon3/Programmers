def solution(n):
    index = [0, 1]
    for i in range(2, n + 1):
        index.append((index[i - 1] + index[i - 2]) % 1234567)
    return index[n]

print(solution(10))