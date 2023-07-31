def dfs(node, n, nn):
    visited, stk, res = [False] * 101, [n], 1
    visited[n] = True
    while stk:
        n = stk.pop()
        for i in node[n]:
            if not visited[i] and i != nn: 
                visited[i], res = True, res + 1
                stk.append(i)
    return res
            
def solution(n, wires):
    node, res = dict([(i, []) for i in range(1, n + 1)]), []
    for w in wires:
        node[w[0]].append(w[1])
        node[w[1]].append(w[0])
    for w in wires:
        tmp1, tmp2 = dfs(node, w[0], w[1]), dfs(node, w[1], w[0])
        res.append(abs(tmp1 - tmp2))
    return min(res)
    
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))