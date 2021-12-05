#### The Greedy Approach
# 최종해답을 찾기 위해 각 단계마다 하나의 답을 고름
# 각 단계에서 답을 고를 때 가장 좋아보이는 답을 선택
# 선택 당시에는 최적의 답을 고름 -> 최종해답이 반드시 최적임을 보장하지 않음
#### 설계전략
# 선택과정: 집합에 추가할 다음 최적의 원소 고름
# 적절성 검사: 새로운 집합이 해답으로 적절한지 검사
# 해답점검: 새로운 집합이 문제의 해답인지 판단
#### 장단점
# +: 설계 쉬움
# -: 최적화 문제에서 반드시 정확성을 증명해야함

#### 최소비용신장트리
# 주어진그래프: G=(V,E): connect, weighted, undirected -> 모든정점이 연결된 가중치가 있는 무방향그래프
# 신장트리(spanning tree): G의 부분그래프 T=(V,F), F는 E에 포함
# ->그래프 G의 모든정점을 연결하는트리: 간선개수는 n-1
# 최소비용 신장트리(MST: minimum spanning tree)
# :모든 신장트리 T중에서 가중치의 합이 최소가 되는 신장트리
#### 이해
# Brute-Foce:모든신장트리 찾아서 가중치의 합 가장적은것 선택
# 간선개수가 n-1인 연결된트리(acyclic)가 될 때 까지 간선 하나씩 제거
# Greedy Approach
# 1. 초기화: 해답집합을 공집합으로 둠
# -> 간선 집합 E의 부분집합 F를 공집합으로 둠
# 2. 선택: 최적의 원소 하나를 해답의 집합에 포함시킴
# -> E에서 최적의 간선 하나를 추출해서 F에 포함시킴 ->프림/크루스칼
# 3. 검사: 해답의 집합이 최종이면 종료 / 아니면 2 반복
# -> 간선의 부분집합 F의 원소갯수가 n-1이면 최종해답

####프림 알고리즘
# 1. F=공집합, Y={v1}(Y: 정점의 집합 V의 부분집합)
# 2. V-Y 집합에서 Y에 가장가까운 정점(vnear) 선택
#    Y집합에 vnear 추가, F집합에 (nearest(vnear),vnear)를추가
# 3. Y=V: Y집합이 V집합의 모든 원소를 포함하면 종료
# W[i][j]:인접행렬(간선의 가중치)
# nearest[i]: Y집합에서 vi에 가장 가까운 정점의 인덱스
# distance[i]: vi와 nearest[i]의 정점을 연결하는 간선의 가중치


####존나 하나도 모르게따!!!!!!!!!!!!!!!!!tlqkf
def prim(W):##W:인접행렬(간선의 가중치)
    ##1. 초기화
    n=len(W)-1
    F=[]
    nearest=[-1]*(n+1)##Y집합에서 vi에 가장 가까운 정점의 인덱스
    distance=[-1]*(n+1)##vi와 nearest[i]의 정점을 연결하는 간선의 가중치
    for i in range(2,n+1):##2~n
        nearest[i]=1##Y집합에서 vi와 가장 가까운 정점이 모두 v1이라고 설정(Y에 v1포함시킴)
        distance[i]=W[1][i]##가장 가까운 정점(v1)과의 가중치 설정
    ##2. 선택
    for _ in range(n-1):##n-1번..? n-2번..?
        minvalue=INF
        for i in range(2, n+1):##2~n
            if(0<=distance[i] and distance[i]<minvalue):##0<=vi~v1까지의거리<=minvalue -> Y에 포함되어있지 않으면
                minvalue=distance[i]##범위 안에 있으면 minvalue 바꾸기
                vnear=i##vnear 설정
        edge=(nearest[vnear],vnear,W[nearest[vnear]][vnear])##v1, vnear, 그 둘(1, vnear)의 가중치 튜플로 만듬
        F.append(edge)##F=[(i,j,w), ...,]->4가 되면 종료
        distance[vnear]=-1##vnear, v1의 가중치: -1로 설정: vnear는 Y에 포함됨
        ##3. 검사
        for i in range(2,n+1):##2~n-2
            if(distance[i]>W[i][vnear]):##vi,Y집합에서 vi에 가장 가까운 정점의 인덱스의 가중치가 진짜 vi, vnear 가중치보다 크면
                distance[i]=W[i][vnear]##가중치 바꾸기(최소로!)
                nearest[i]=vnear##Y집합에서 vi와 가장 가까운 정점 v1->vi로 바꾸기
    return F
def cost (F):
    total = 0
    for e in F:
        total += e[2]
    return total
def print_nd (F, nearest, distance): 
    print('F = ', end = '')
    print(F)
    print(' nearest: ', end = '')
    print(nearest)
    print('  distance: ', end = '')
    print(distance)
INF = 999 
W=[[-1, -1, -1, -1, -1], [-1, 0, 1, 3, INF, INF], [-1, 1, 0, 3, 6, INF], [-1, 3, 3, 0, 4, 2], [-1, INF, 6, 4, 0, 5], [-1, INF, INF, 2, 5, 0]]
F = prim(W)
for i in range(len(F)):
    print(F[i])
print("Minimum Cost is ", cost(F))