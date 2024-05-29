'''
뱀

사과를 먹으면 뱀 길이가 늘어남
벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남

게임은 N x N 정사각 보드 위에서 진행되고, 
몇몇 칸에는 사과가 놓여져 있습니다. 
보드의 상하좌우 끝에는 벽이 있습니다
게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1
뱀은 처음에 오른쪽을 향한다

규칙)
1. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킵니다.
2. 만약 이동한 칸에 사과가 있다면, 
    그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 
    즉, 몸길이는 변하지 않습니다.

사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하세요.

입력)
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
출력)
9

입력)
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
출력)
21
'''
import sys

n = int(input())    # 보드 크기
k = int(input())    # 사과 갯수
mapArray = [[0]*(n+1) for _ in range(n+1)]    # 보드

for _ in range(k):
    a, b = map(int, input().split(" "))
    mapArray[a][b] = 1    # 사과 위치

l = int(input())    # 뱀의 방향 전환 횟수
rotateList = []     # 방향 정보 저장 List
for _ in range(l):
    x, c = sys.stdin.readline().strip().split(" ")    # x초 후 c방향으로 90도 회전
    rotateList.append([int(x), c])

# 뱀은 처음에 오른쪽을 향한다. 동,남,서,북 
movingDir = [[0, 1],[1, 0], [0, -1], [-1, 0] ]

def solution(mapArray):
    x, y = 1, 1    # 시작 좌표
    mapArray[x][y] = 2    # 뱀 초기 위치
    dir = 0        # 처음 방향, 동쪽
    time = 0       # 뱀이 움직이는 시간

    que = [[x, y]]    # 처음 뱀 머리 위치

    while que:    # 뱀 이동
        
        # 머리를 다음 칸에 위치
        nx = x + movingDir[dir][0]    
        ny = y + movingDir[dir][1]
        time +=1

        if(0<=nx<=n and 0<=ny<=n and mapArray[nx][ny] != 2): 
            if(mapArray[nx][ny] == 0):    # 사과가 없으면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
                que.append([nx, ny])      # 머리를 이동
                mapArray[nx][ny] = 2      
                tailX, tailY = que.pop(0)    
                mapArray[tailX][tailY] = 0   
            elif(mapArray[nx][ny] == 1):    # 사과 있으면, 사과가 없어지고 꼬리는 움직이지 않음
                que.append([nx, ny])        # 머리 이동
                mapArray[nx][ny] = 2

            x, y = nx, ny    # 위치 업데이트

        else:    # 벽이나 몸에 부딪히는 경우
            break


        if len(rotateList)>0 and time == rotateList[0][0]:    # 방향 전환이 남아있고 움직여야할 시간일 경우
            if c == 'L':    # 다음 전환 방향이 왼쪽이면, 반시계방향으로 회전
                dir = (dir-1)%4    # 동->북->서->남
            elif c== 'D':   # 다음 전환 방향이 오른쪽이면, 시계방향 회전
                dir = (dir+1)%4    # 동->남->서->북
            rotateList.pop(0)

    print(time)     

    return 

solution(mapArray)

'''
# https://www.acmicpc.net/problem/3190
from collections import deque
APPLE = 5

def solution(n, A, move) :
    time = 1
    snake = deque([(1,1)])
    direct = deque([(0,1),(1,0),(0,-1),(-1,0)])

    while move :
        mv = move.popleft()

        # mv[1]에 들어있는건 예비 방향임(다음 번에 틀 방향인거지, 현재 이 방향으로 가고 있는 게 아님).
        while time <= mv[0] :
            ny = snake[-1][0] + direct[0][0]
            nx = snake[-1][1] + direct[0][1]

            if (ny < 1) or (ny > n) or (nx < 1) or (nx > n) or A[ny][
'''