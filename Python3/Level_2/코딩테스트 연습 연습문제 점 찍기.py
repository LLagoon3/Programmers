def solution(k, d):
    onc = 0
    for x in range(0, d + 1, k):
        y = ((d ** 2) - (x ** 2)) ** 0.5
        print(y)
        onc += int (y // k) + 1
    return onc
        
print(solution(1, 5))

# ((x ** 2) + (y ** 2)) <= d ** 2