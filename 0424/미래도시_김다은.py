INF = int(1e9)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''

def solution(n, m, k, x, distance) :

    for h in range(1, n + 1) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                distance[i][j] = min(distance[i][j], distance[i][h] + distance[h][j])

    result = distance[1][x] + distance[x][k]

    if result == INF :
        return -1
    else :
        return result

n, m = map(int, input().split())
distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(1, n+1) :
    distance[_][_] = 0

for _ in range(m) :
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

k, x = map(int, input().split())

# n, m = 5, 7
# k, x = 4, 5
# distance = [[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
#  [1000000000, 0,            1,          1,          1,      1000000000],
#  [1000000000, 1,            0,          1000000000, 1,      1000000000],
#  [1000000000, 1,            1000000000, 0,          1,      1],
#  [1000000000, 1,            1,          1,          0,      1],
#  [1000000000, 1000000000,   1000000000, 1,          1,      0]]

print(solution(n, m, k, x, distance))
