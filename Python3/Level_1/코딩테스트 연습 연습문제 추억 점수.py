def solution(name, yearning, photo):
    index, arr = dict(list(zip(name, yearning))), list()
    for p in photo: arr.append(sum(list(map(lambda x: index[x] if x in index else 0, p))))        
    return arr

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))