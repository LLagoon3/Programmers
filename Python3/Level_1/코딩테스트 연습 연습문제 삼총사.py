def solution(number):
    number, res = sorted(number), 0
    for ptr0 in range(0, len(number)):
        if number[ptr0] > 0: break
        for ptr1 in range(ptr0 + 1, len(number)):
            for ptr2 in range(ptr1 + 1, len(number)):
                if number[ptr1] + number[ptr2] == -number[ptr0]:
                    res += 1
                    print(number[ptr0], number[ptr1], number[ptr2])
    return res
    
print(solution([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]))
print(solution([0, 0, 0, 0, 0]))
        