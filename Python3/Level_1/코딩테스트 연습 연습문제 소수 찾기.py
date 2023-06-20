import math
def chk(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def solution(n):
    res = 0
    for i in range(2, n + 1):
        if chk(i):res += 1
    return res

def solution(n):
    import math
    index = set()
    for i in range(2, n + 1): index.add(i)
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(2, (n // i) + 1): 
            if (i * j) in index: index.remove(i * j)
    return (index)

print(solution(5))