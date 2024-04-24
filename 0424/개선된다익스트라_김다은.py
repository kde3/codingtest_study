import heapq
INF = 1e9

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

def solution(start, graph, distance) :
    queue = []

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue :
        dist, now = heapq.heappop(queue)

        if distance[now] < dist :
            continue

        for g in graph[now] :
            cost = dist + g[1]

            if cost < distance[g[0]] :
                distance[g[0]] = cost
                heapq.heappush(queue, (cost, g[0]))

    return distance

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# n, m = 6, 11
# start = 1
# graph = [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]
# distance = [1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0]
print(solution(start, graph, distance))