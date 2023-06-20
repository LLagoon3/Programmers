s = ["Jane", "Kim"]

def solution(s):
    for index, n in enumerate(s): 
        if n == 'Kim': return "김서방은 {0}에 있다".format(index)
