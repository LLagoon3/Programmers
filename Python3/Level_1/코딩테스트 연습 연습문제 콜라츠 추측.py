def solution(num):
    cnt = 0
    while num != 1:
        if cnt > 500: return -1
        num = (lambda x : x // 2 if x % 2 == 0 else x * 3 + 1)(num)
        cnt += 1
    return cnt
print(solution(6))