#https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3

input = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
# input =  [[1,10],[1,2],[2,3],[3,4]]
def solution(targets):
    res = dict()
    while targets:
        tg = targets.pop()
        m, min_i, min_s, min_e = 100000000, -1, -1, -1
        for index, cmp in res.items():
            s, e = max([tg[0], cmp[0]]), min([tg[1], cmp[1]])
            if e - s > 0 and e - s < m:
                m, min_i, min_s, min_e= e - s, index, s, e
        if min_i == -1: res[len(res)] = tg
        else:
            res[min_i] = [min_s, min_e]
    print(res)
    return len(res)

def solution_(target):
    res = [0]
    for s, e in sorted(target):
        if res[-1] <= s: res.append(e)
        else: res.append(min(res.pop(), e))
    return len(res) - 1

print(solution_(input))

# def solution(targets):
#     res = dict()
#     while targets:
#         tg = targets.pop()
#         m, min_i, min_s, min_e = 100000000, -1, -1, -1
#         for index, cmp in res.items():
#             s, e = max([tg[0], cmp[0]]), min([tg[1], cmp[1]])
#             if e - s > 0 and e - s < m:
#                 m, min_i, min_s, min_e= e - s, index, s, e
#         if min_i == -1: res[len(res)] = tg
#         else:
#             del res[min_i]
#             res[len(res)] = [min_s, min_e]

#     return len(res)