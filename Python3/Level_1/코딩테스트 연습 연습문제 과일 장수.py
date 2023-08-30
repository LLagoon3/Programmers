def solution(k, m, score):
    score = sorted(score)
    cnt, res = 0, 0
    while score:
        cnt += 1
        if cnt == m:
            cnt, res = 0, res + (score.pop() * m)
        else:
            score.pop()
    return res
    
print(solution(3, 4, [0, 1, 2, 3, 1]))