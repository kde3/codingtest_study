'''
문제 2)

신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는
 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 
3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.

하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 
영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력)        출력)
7              4
6
1 2
2 3
1 5
5 2
5 6
4 7 
'''
from collections import deque

# n = int(input())    # 컴퓨터 수
# m = int(input())    # 연결 수
n = 7
m = 6
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)    # 무방향이기 때문에 양쪽으로 추가해야 함


visit = [False]*(n+1)

def bfs(graph, visit, idx):
    cnt = 0
    que = deque([idx])
    visit[idx] = True

    while que:
        cur = que.popleft()

        for i in graph[cur]:
            if visit[i] == False:
                que.append(i)
                visit[i] = True
                cnt += 1
    
    print(cnt)

    return 

def solution(graph, visit):
    start = 1
    bfs(graph, visit, start)

    return 

solution(graph, visit)