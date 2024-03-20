from collections import deque

def bfs(n, k) :
    queue = deque([n])
    visited = [0 for _ in range(100001)]  # 인덱스가 아니라 '번째'이기 때문에 +1을 해야 100000까지 다 생성됨.
    
    while queue :
        q = queue.popleft()
        
        if q == k :
            return visited[q]
        
        for i in [q-1, q+1, q*2] :
            if 0 <= i <= 100000 and visited[i] == 0 :
                queue.append(i)
                visited[i] += visited[q] + 1
                
n, k = map(int, input().split())
# n, k  = 5, 17
print(bfs(n, k))