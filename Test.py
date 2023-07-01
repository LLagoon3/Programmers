# 가위(0), 바위(1), 보(2)
# 두 개의 입력일 때 (0, 1) 중 누가 이길지, 비기면 -1

def solution(a, b):
    index = [1, 2, 3]
    if (a - 1) % 3 == b: return 0
    elif (a + 1) % 3 == b: return 1
    return -1

print(solution(2, 0)) 


####

