

def solution(n, wires):
    node = dict([(i, []) for i in range(1, n + 1)])
    for w in wires:
        node[w[0]].append(w[1])
        node[w[1]].append(w[0])
    print(node)
    
print(solution(4, [[1,2],[2,3],[3,4]]))