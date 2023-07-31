def solution(phone_book):
    index, phone_book = dict(), sorted(phone_book)
    for n in phone_book:
        tmp = ''
        for i in n:
            tmp += i
            if tmp in index: return False
        index[tmp] = True
    return True

print(solution(["1195524421", "97674223", "119"]	))