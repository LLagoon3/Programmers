a, b = [1, 4, 2], [5, 4, 4]

# def solution(a, b):
#     res = []
#     for i in range(0, len(a)):
#         tmp = []
#         for j in range(0, len(b)):
#             if not res: tmp.append(b[j] * a[i])
#             else:
#                 min = 1001
#                 for index, bn in enumerate(res[i - 1]):
#                     if index != j and min > bn: min = bn
#                 tmp.append(min + (b[j] * a[i]))
#             res.append(tmp)
#     print(tmp)

def solution(a, b):
    a, b, res = sorted(a), sorted(b), 0
    for an in a:
        res += an * b.pop()
    return res
    
print(solution(a, b))