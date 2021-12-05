# Dk:k개의 중간 정점을 지나는 최단경로길이의 행렬
# Dk[i][j]:vi~vj로 k개의 중간정점을 지나는 최단경로 길이
# D0:다른 어떤 정점도 지나지 않는 최단경로의 길이(=W)
# Dn:다른 모든 정점을 지날 수 있는 최단경로의 길이(=D)
##### 재귀 관계식
# D0=W
# Dk[i][j]=min(Dk-1[i][j], Dk-1[i][k]+Dk-1[k][j])   
# ->하나의 정점을 더 지나게 해 줘도 새로운 최단경로가 없는 경우/하나의정점(vk)를 더 지나면 새로운 최단경로가 있는 경우 중 최소값이 k개의 정점을 지나는 새로운 최단경로
def floyd(W):##최단경로의 길이만 구함
    D=W##최단경로 길이의 행렬
    n=len(W)##W의 길이
    for k in range(n):##0~n-1
        for i in range(n):##0~n-1
            for j in range(n):##0~n-1
                D[i][j]=min(D[i][j],D[i][k]+D[k][j])##둘 중 작은 값으로 덮어쓰기
    return D
INF=999
W=[[0,1,INF,1,5],[9,0,3,2,INF],[INF,INF,0,4,INF],[INF,INF,2,0,3],[3,INF,INF,INF,0]]##-->len(W)=6   ([]의 갯수)
# D=floyd(W)
# for i in range(len(D)):
#     print(D[i])

##### 최단경로를 구하기 위해서는 그 과정 기록해야 함(위에서는 최단경로의 길이만 구함)
# P[i][j]:vi~vj로 가는 최단경로가 거쳐야 하는 새로운 정점
# ->vi~vj로 가는 최단경로의 중간에 놓여있는 정점이 최소한 하나가 있는 경우: 그 놓여있는 정점 중 가장 큰 인덱스
# ->최단경로의 중간에 놓여있는 정점이 없는 경우: -1
def floyd2(W):##최단경로를 구함
    n=len(W)
    D=W
    P=[[-1]*n for _ in range(n)]##[[-1,-1,...,-1(-1 n개,[-1,...,-1],...,[-1,...,-1]]([] n개)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(D[i][j]>D[i][k]+D[k][j]):##k를 거쳐가는 경로가 최단경로라면
                    D[i][j]=D[i][k]+D[k][j]##D[i][j] 수정
                    P[i][j]=k##P[i][j] 수정(k를 거쳐감 표시해줌, k는 놓여있는 정점 중 가장 큰 인덱스)
                ## k를 거치지 않는 경우가 최단경로라면 D[i][j], P[i][j] 업데이트 안해줘도댐
    return D,P
#### P[i][j]=-1   ->(vi, vj)가 최단경로
#### P[i][j]=k   ->inorder 탐색
#### (vi, vk)최단경로 출력   ->vk출력   ->(vk, vj)최단경로 출력
def path(P,u,v):
    if(P[u][v]!=-1):##(vi, vj)가 최단경로가 아님 ->inorder탐색
        path(P,u,P[u][v])##P[u][v]=k   재귀(vu~vk)
        print('v%d'%(P[u][v]),end='->')
        path(P,P[u][v],v)##P[u][v]=k   재귀(vk~vj)
    #### (vi, vj)가 최단경로인 경우: 아무일 ㄴㄴ 그냥 최단경로인 거임 ㅅㄱ
D,P=floyd2(W)
for i in range(len(D)):
    print(D[i])
for i in range(len(P)):
    print(P[i])
##v4->v2인 경우
u=4
v=2
print('shortest path from v%d to v%d: '%(u,v),end='')
print('v%d'%(u),end='->')
path(P,u,v)
print('v%d'%(v),end='')