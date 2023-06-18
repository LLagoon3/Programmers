arr = [1,1,3,3,0,1,1]

def solution(arr):
    stack = [-1]
    for n in arr:
        tmp = stack.pop()
        if tmp == n: stack.append(tmp)
        else:
            if tmp != -1: stack.append(tmp) 
            stack.append(n)
    return stack

print(solution(arr))