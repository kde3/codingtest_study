'''
문제1)

수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력)      출력)
5 17        4
'''

from collections import deque

INF = int(1e9)
#n, k = map(int, input().split())
n = 5
k = 17

dist = [0]*100001    # INF말고 최대값 처리해야 함

def dfs(n, k):
    que = deque()
    que.append(n)
    timeCnt = 0
    
    while que:
        x = que.popleft()            # 5
        
        nextMove = [x+1, x-1, x*2]   # 6, 4, 10

        if x==k:
            break

        for next in nextMove:
            if 0<= next <= 100000 and dist[next] == 0:
               dist[next] = dist[x]+1    
               que.append(next)
               print(next, dist[next], dist[x])
        
    #print(que)
    print(dist[x])
    return 

def solution(n, k):

    dfs(n, k)

    return 

solution(n, k)