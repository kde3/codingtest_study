'''
문제2
n*m크기 행렬에 내구도를 가진 건물이 각 칸마다 하나씩
적의 공격 받으면 내구도 감소, 0 이하면 파괴
아군의 회복 받으면 내구도 상승
적 공격과 아군 회복은 항상 직사각형

건물이 파괴되었다가 복구가능
내구도가 0 이하가 된 이미 파괴된 건물도
공격을 받으면 계속해서 내구도가 하락
'''
# n, m = map(int, input().split())
# board = [[0]*m for _ in range(n)]
# for _ in range(n):
#     board = list(map(int, input().split()))

# skill = [[0]*m for _ in range(n)]
# for _ in range(n):
#     skill = list(map(int, input().split()))

from collections import Counter


result = 0

board = [[5, 5, 5, 5, 5],
         [5, 5, 5, 5, 5],
         [5, 5, 5, 5, 5],
         [5, 5, 5, 5, 5]]

skill = [[1,0,0,3,4,4],
         [1,2,0,2,3,2],
         [2,1,0,3,1,2],
         [1,0,1,3,3,1]]

def solution(board, skill):
    answer = 0
    
    for typeValue, r1, c1, r2, c2, degree in skill:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if typeValue == 1:
                    board[i][j] -= degree
                else:
                    board[i][j] += degree

    for i in range(len(board)):
        print(board[i])
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    print(answer)

    return answer

solution(board, skill)


'''
답)
누적합으로 풀어야 함
아니면 효율성이 낮음
'''