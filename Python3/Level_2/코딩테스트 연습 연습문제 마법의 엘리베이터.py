def solution(storey):
    index, cnt = list(map(int, str(storey))), 0
    while index:
        tmp = index.pop()
        if tmp > 5:
            if index == []: index.append(1)
            else: index[-1] += 1
            cnt += 10 - tmp
        elif tmp == 5:
            if index != [] and index[-1] >= 5:index[-1] += 1
            cnt += 10 - tmp
        else: cnt += tmp
    return cnt

print(solution(93))