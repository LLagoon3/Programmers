def solution(n, works):
    works, tmpn = sorted(works, reverse=True), 0
    for i in range(1, len(works)):
        a, b = works[i - 1], works[i]
        c = a - b
        if c > n:
            tmp = c - n
            tmp = ((a ** 2) * i) + ((b - tmp) ** 2)
            for j in range(i + 2, len(works)): tmp += works[j] ** 2
            return tmp
        if tmpn + (c * i) > n:
            tmp = tmpn + (c * i) - n
            tmp1 = (i + 1 - tmp) * a + (tmp * b)
            for j in range(tmp + 1, len(works)): tmp1 += works[j] ** 2
            return tmp1
        elif tmpn + (c * i) == n:
            tmp = 0
            for j in range(i + 1, len(works)): tmp += works[j] ** 2
            return tmp + (b * (i + 1))
        else: tmpn += (c * i)
        # print(a, b, c, tmpn)
    n = n - tmpn
    tmp1, tmp2 = n // len(works), n % len(works)
    w = b - tmp1
    if w <= 0: return 0
    return ((w ** 2) * (len(works) - tmp2)) + (((w - 1) ** 2) * tmp2)
    
def solution(n, works):
    def calResWithNum(bnum, anum, index):
        return ((bnum ** 2) * index) + ((anum ** 2) * (len(works) - index))
    def calResWithList(bnum, anumList, index):
        tmp = sum(anumList[index + 1:])
        return ((bnum ** 2) * index) + tmp
    works = sorted(works, reverse= True)
    for i in range(1, len(works)):
        bnum, nnum = works[i - 1], works[i]
        ntmp = nnum - bnum
        if ntmp > n:
            if i - 2 >= 0: return sum(works[:i - 1]) + (bnum - ntmp + n) + sum(works[i:])
            else: return (bnum - ntmp + n) + sum(works[i:])
        
                
                
# print(solution( 1, [8, 1]))
# print(solution(12, [2, 5, 4, 3, 3]))
        
        
        
        