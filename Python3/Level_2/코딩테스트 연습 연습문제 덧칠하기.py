#https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    last_pos = 1
    for pos in section:
        if last_pos > pos:
            continue
        last_pos = pos + m
        answer += 1
        
    return answer
