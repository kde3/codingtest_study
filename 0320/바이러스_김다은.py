from collections import deque

def bfs(n, k, graph) :
    visited = [0 for _ in range(n+1)]
    queue = deque([1])
    
    while queue :
        q = queue.popleft()
        visited[1] = 1
        
        for g in graph :
            if q == g[0] and visited[g[1]] == 0:
                queue.append(g[1])
                visited[g[1]] += 1
#     print(visited)
    return sum(visited)-1

        
# =========================
n = int(input())
k = int(input())

graph = []
for _ in range(k) :
    a, b = map(int, input().split())
    graph.append([a, b])
#     if a != 1 :
#         graph.append([b, a])
    graph.append([b, a])
    
print(bfs(n, k, graph))