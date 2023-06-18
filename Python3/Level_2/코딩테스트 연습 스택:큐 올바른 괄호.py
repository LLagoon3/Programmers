s = ")()("

def solution(s):
    stack = []
    for c in s:
        if c == ')':
            if stack and stack.pop() == '(': continue
            else: return False
        else: stack.append(c)
    if not stack: return True
    else: return False
    
print(solution(s))