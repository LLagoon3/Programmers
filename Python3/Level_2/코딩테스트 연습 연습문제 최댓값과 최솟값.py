s = "1 2 3 4"

def solution(s):
    s = list(map(lambda x: int(x), s.split(" ")))
    return "{0} {1}".format(min(s), max(s))
    
print(solution(s))