nums = [3,1,2,3]

def solution(nums):
    tp = len(set(nums))
    if tp >= len(nums) // 2: answer = len(nums) // 2
    else: answer = tp
    return answer

print(solution(nums))
