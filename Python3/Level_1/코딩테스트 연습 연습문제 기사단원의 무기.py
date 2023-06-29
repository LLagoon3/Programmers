
def solution(number, limit, power):
    index = 0
    for n in range(1, number + 1):
        tmpindex = 2
        if (n ** 0.5) % 1 == 0: tmpindex -= 1
        for nn in range(2, int(n ** 0.5) + 1):
            if n % nn == 0: tmpindex += 2
            if tmpindex > limit:
                tmpindex = power
                break
        index += tmpindex
    return index

print(solution(10, 3, 2))