n, k= 5, 3
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]

def solution(N, road, K):
    graph, res, visited = {1: 0}, 0, []
    for i in range(2, N + 1):
        graph[i] = 500001
    for i in range(0, N):
        index, v = 0, 500001
        for key, val in graph.items():
            if key not in visited and val < v: index, v = key, val
        visited.append(index)
        for r in road:
            if r[0] == index and graph[r[1]] > graph[index] + r[2]: graph[r[1]] = graph[index] + r[2]
            elif r[1] == index and graph[r[0]] > graph[index] + r[2]: graph[r[0]] = graph[index] + r[2]
            # print("i : ", index, "  graph : ", graph)
    for key, val in graph.items():
        if val <= K: res += 1
    return res

print(solution(n, road, k))