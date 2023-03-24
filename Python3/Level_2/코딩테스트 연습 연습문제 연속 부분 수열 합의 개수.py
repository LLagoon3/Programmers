#https://school.programmers.co.kr/learn/courses/30/lessons/131701?language=python3

def _solution(elements):
    answer = set()
    tmp_last = 0
    for i in range(0, len(elements) - 1):
        for j in range(0, len(elements)):
            tmp = 0
            for k in range(j, j + i + 1):
                if k >= len(elements): index = k - len(elements)
                else: index = k
                tmp += elements[index]
            answer.add(tmp)
        tmp_last += elements[i]
    answer.add(tmp_last + elements[-1])
    return len(answer)

def solution(elements):
    answer = set()
    for i in range(0, len(elements)):
        tmp = 0
        for j in range(0, len(elements) - 1):
            if i + j >= len(elements): index = i + j - len(elements)
            else: index = i + j
            tmp += elements[index]
            answer.add(tmp)
        if i == 0:answer.add(tmp + elements[-1])
    return len(answer)

print(solution([7,9,1,1,4]))