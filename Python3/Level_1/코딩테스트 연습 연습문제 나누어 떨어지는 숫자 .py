arr = [5, 9, 7, 10]

def solution(arr, divisor):
    if divisor == 1: return sorted(arr)
    answer = []
    for n in sorted(arr):
        if n % divisor == 0: 
            answer.append(n)
    if not answer: return [-1]
    return answer

print(solution(arr, 5))
