a, b,  = 1, 2

def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    st = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    sday = 0
    for i in range(0, a - 1): sday += day[i]
    sday += b
    answer = st[(5 + ((sday % 7) - 1)) % 7]
    return answer

print(solution(a, b))