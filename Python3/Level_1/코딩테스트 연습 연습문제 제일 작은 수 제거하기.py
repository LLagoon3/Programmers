arr = [10]
def solution(arr):
    m = min(arr)
    return list(i for i in arr if i != m) if len(arr) != 1 else [-1]

print(solution(arr))