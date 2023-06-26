def solution(arr):
    a = arr.pop()
    while arr:
        b = arr.pop()
        if a == b: continue
        for i in range(int((max(a, b) // 2) + 1), 0, -1):
            if a % i == 0 and b % i == 0:
                a = (a // i) * (b // i) * i
                break
    return a
        
        
print(solution([4, 4]))
        