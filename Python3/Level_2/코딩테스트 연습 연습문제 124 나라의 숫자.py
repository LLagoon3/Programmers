n = 18
#141

# def solution(n):
#     index = ['1', '2', '4']
#     answer = ''
#     answer += index[(n - 1) % 3]
#     n -= 1
#     if int(n / 3) == 0: return answer
#     while 1:
#         n = int(n / 3)
#         if n <= 3:
#             answer = index[n - 1] + answer
#             break
#         else: answer = index[(n % 3) - 1] + answer
#     return answer

def solution(n):
    index = ['-1', '1', '2', '4']
    answer = ''
    b = False
    while 1:
        g = n % 3
        n = int(n / 3)
        
        if b == True: 
            g -= 1
            b = False
        if g <= 0 and n != 0:
            g += -1
            b = True
        if g <= 0 and n == 0:
            break
        answer = index[g] + answer
        if n == 0: break
            
    return answer


print(solution(n))