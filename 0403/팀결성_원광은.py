'''
문제1)
팀결성

학생들에게 0부터 n까지 번호 부여
처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 n+1개 팀
'팀 합치기', '같은 팀 여부 확인' 연산
팀 합치기 : 두 팀을 합치는 연산
같은 팀 여부 확인 : 특정한 두 학생이 같은 팀에 속하는지 확인

m개의 연산을 수행할 때 '같은 팀 여부 확인' 연산에 대한 결과 출력

0 : 팀 합치기
1 : 같은 팀 여부 확인

입력)
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력)
no
no
yes
'''

n, m = map(int, input().split(" "))

inputList = []
for i in range(m):
    inputData = list(map(int, input().split(" ")))
    inputList.append(inputData)

parent = [0] * (n+1)    # 부모 테이블
for i in range(n+1):
    parent[i] = i       # 처음에는 노드가 연결되어 있지 않으므로 각각의 노드가 대표 노드

 # a, b 원소가 속한 집합을 합친다
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a < b:    # 노드가 작은 원소가 부모노드가 되도록
        parent[b] = a
    else:
        parent[a] = b

    return

# 해당 idx의 루트 노드를 찾을때까지 부모테이블을 재귀적 호출
def findParent(parent, idx):
    if parent[idx] != idx:
        return findParent(parent, parent[idx])
   
    return idx

def solution(inputList):
    print(inputList)
    for i in range(len(inputList)):
        if inputList[i][0] == 0:    # 팀 합치기
        #    print("union")
            unionParent(parent, inputList[i][1], inputList[i][2])
        elif inputList[i][0] == 1:  # 같은 팀 여부 확인
        #    print("find")
            if findParent(parent, inputList[i][1]) == findParent(parent, inputList[i][2]):
                print("yes")
            else:
                print("no")
    return 

solution(inputList)


'''
union-find 로 구현
트리 구조
https://doing7.tistory.com/82
사이클 발생 여부 확인해서 효율 높힐 수 있음
'''
