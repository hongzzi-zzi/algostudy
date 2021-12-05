#### 연쇄 행렬 곱셈: 동적계획(Dynamic Programming)
# 1. 재귀 관계식 찾기
#  M: 연쇄 행렬을 곱하는데 필요한 곱셈의 최소 횟수 행렬
#  M[i][j]:Ai~Aj행렬을 곱하는데 필요한 곱셈의 최소 횟수(1<=i<=j<=n)
#  ->Ai~Aj행렬을 (Ai*...*Ak)(Ak+1*...*Aj)로 분할하는 재귀 관계식 찾기
# 2. 상향식 방법으로 해답 구하기
#  초기화:M[i][i]=0(주대각선을 0으로)
#  최종 목표:M[1][n]
#  상향식 계산: 대각선 1번, 대각선 2번, ...., 대각선 n-1번

#### 연쇄 행렬 곱셈의 재귀 관계식 구하기
# 분할정복   -> n개의 행렬을 최적 부분행렬의 곱으로 분할
# 각 분할의 곱셈횟수: 각 부분행렬의 곱셈횟수+두행렬의 곱셈횟수
#   -> M[1][k]+M[k+1][6](각 부분행렬의 곱셈횟수)+d0dkd6(두 행렬의 곱셈횟수)
#       Ak−1의 행(가로)의 개수와 Ak의 열(세로)의 개수가 같아야함   ->그래야 행렬곱셈 가능
#       dk: 행렬 Ak의 행의 개수(=Ak+1의 열의 개수) / d0=A1의 열의 개수
#       일반적으로 i*k행렬과 k*j행렬을 곱하면 i*j행렬이나옴, 원소곱셈의 횟수: i*k*j
#       ->d0dkd6=A1의 열*Ak의 행(=Ak+1의 열)*A6의 열
# 최적 분할: M[1][6]=minimum(M[1][k]+M[k+1][6]+d0dkd6)

#### 연쇄 행렬 곱셈의 재귀 관계식
# for 1<=i<=j<=n
# if i+j, M[i][j]=0
# if i<j, M[i][j]=minimum(M[i][k]+M[k+1][j]+di-1dkdj)
def minmult(d):
    n=len(d)-1
    M=[[-1]*(n+1)for _ in range(n+1)]
    P=[[-1]*(n+1)for _ in range(n+1)]##[[-1,-1,...,-1(-1 n+1개)],...,[-1,...-1]([] n+1개)]
    for i in range(1,n+1):
        M[i][i]=0##초기화(주대각선을 0으로)
    for diagonal in range(1,n):##1~n-1
        for i in range(1,n-diagonal+1):##1~n-diagonal
            j=i+diagonal
            M[i][j],P[i][j]=minimum(M,d,i,j)##minimum정의해주기
    return M,P

def minimum(M,d,i,j):
    minValue=INF
    minK=0
    for k in range(i,j):##i~j-1
        value=M[i][k]+M[k+1][j]
        value+=d[i-1]*d[k]*d[j]##value=M[i][k]+M[k+1][j]+d[i-1]*d[k]*d[j]
        if(minValue>value):##INF>value=M[i][k]+M[k+1][j]+d[i-1]*d[k]*d[j]일때
            minValue=value
            minK=k
    return minValue,minK
## 곱셈 순서 
# P[i][j]=k이면, (Ai*...*Ak)(Ak+1*...*Aj)로 분할
# 재귀호출: 분할정복
def order(P,i,j):
    if(i==j):
        print('A%d'%(i),end='')
    else:
        k=P[i][j]
        print('(',end='')
        order(P,i,k)
        order(P,k+1,j)
        print(')',end='')
INF=999
d=[5,2,3,4,6,7,8]
M,P=minmult(d)
print('M= ')
for i in range(1,len(M)):
    print(M[i][1:])
print('P= ')
for i in range(1,len(P)):
    print(P[i][1:])
print('minimum order: ',end='')
order(P,1,len(d)-1)
