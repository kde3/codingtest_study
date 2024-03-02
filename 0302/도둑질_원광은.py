'''
문제1

마을의 집들은 동그랗게 이어져있다
서로 인접한 집을 동시에 도둑질하면 경보가 울린다
각 집에 있는 돈이 담긴 배열 money가 주어진다
도둑이 훔칠 수 있는 돈을 최대값은?

ex)
money = [1, 2, 3, 1]
result = 4

         0   1   2   3    4    5    6 -> 0으로 다시 연결
money = [1, 60, 700, 800, 500, 100, 2] 
0, 2, 4    -> 1201  [1, 700, 500]
0, 2, 5    -> 801   [1, 700, 100]
0, 3, 5    -> 901   [1, 800, 100]
1, 3, 5    -> 960   [60, 800, 100]
2, 4, 6    -> 1202  [700, 500, 2]

'''

#money = list(map(int, input().split()))
#money = [1, 2, 3, 1]
money = [1, 60, 700, 800, 500, 100, 2]
tmp1 = [0]*(len(money)-1) # 첫번째 포함 and 마지막 미포함 
tmp2 =[0]*len(money)  # 첫번째 미포함 and 마지막 포함

def solution(money):   
    tmp1[0] = money[0]    # 첫번째 집 포함
    tmp1[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        tmp1[i] = max(tmp1[i-2]+money[i], tmp1[i-1])  

    tmp2[0] = 0           # 첫번째 집 미포함
    tmp1[1] = max(money[0], money[1])
    for i in range(2, len(money)):
        tmp2[i] = max(tmp2[i-2]+money[i], tmp2[i-1])

    print(tmp1)
    print(tmp2)
    
    result = max(tmp1[-2], tmp2[-1])
    print(result)

    return 

solution(money)
