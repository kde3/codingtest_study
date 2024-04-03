'''
문제2)
도시 분할 계획

n개의 집, m개의 길, 길을 유지하는 유지비용
마을을 2개의 분리된 마을로 분할할 계획
각 분리된 마을 안에 집들이 서로 연결되도록
각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재
마을에는 집이 하나 이상 존재

분리된 두 마을 사이에 있는 길들은 필요없으므로 없앰
각 분리도니 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하므로
길을 더 없앰

나머지 길 유지비 합의 최소값을 반환

입력예)
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

출력)
8
'''

n, m = map(int, input().split())    # n : 집, m : 길

edges = []    # 크루스칼 알고리즘에서 간선을 기준으로 저장하는 배열
for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append([w, s, e])
#print(graph)

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

def solution(edges):
    result = 0
    maxEdge = 0        # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

    edges.sort()       # 간선을 기준으로 그래프 오름차순 정렬 -> 가장 거리가 짧은 간선부터 차례대로 집합에 추가
 
    for cost, s, e in edges:
        if findParent(parent, s) != findParent(parent, e):    # 한 그룹에 포함되어있지 않으면 집합에 포함시킨다.
            unionParent(parent, s, e)
            result += cost
            maxEdge = cost

    print(result-maxEdge)
    return 

solution(edges)


'''
크루스칼 알고리즘 : 최소 신장 트리를 찾는 알고리즘
최소 신장 트리 : 가장 적은 비용으로, 사이클 없이, 모든 정점을 연결하는 알고리즘

모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함
단, 사이클을 발생시키는 간선은 집합에 포함시키지 않음
'''