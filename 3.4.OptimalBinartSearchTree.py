####최적이진검색트리 - 주어진 n개의 키로 최적 이진검색트리를 구하시오
# 주어진 n개의 키: K1, ..., Kn
# 각 키의 검색확률: pi(전체 검색횟수 중 Ki를 검색하는 확률)
# 각 키의 비교횟수: ci(Ki를 검색하는데 필요한 키의 비교횟수)
# 각 키의 평균검색비용(시간):검색확률*비교횟수   ->pi*ci
# 전체 키의 평균검색비용(시간): Tavg=p1*c1+p2*c2+...+pn*cn

#### 이진검색트리(BST:Binary Search Tree)
# 각 노드는 하나의 유일한 키 가짐
# 모든 노드가 가진 키값은 그 노드의 왼쪽 서브트리의 키값보다 큼
# 모든 노드가 가진 키값은 그 노드의 오른쪽 서브트리의 키값보다 작음

#### 최적 이진검색트리: Brute-Force Approach
# 모든 경우의 수 계산
# 카탈란수:C(n)=1/n+1*2nCn~4^n/(n^3/2*(파이)^1/2)
# n개의 키로 만들 수 있는 이진트리수=C(n)

#### 최적 이진검색트리: Dynamic Programming
# 1. 재귀 관계식 찾기
#   A:이진검색트리를 만드는데 최적검색비용의 행렬
#   A[i][j]:Ki~Kj 이진검색트리를 만드는데 최적검색비용
#   목표: Ki~Kj를 (Ki...Kk-1)Kk(Kk+1...Kj)로 분할하는 재귀관계식 찾기
# 2. 상향식 방법으로 해답구하기
#   초기화:A[i][j]=pi(주대각선을 pi로)
#   최종목표: A[1][n]
#   상향식 계산: 대각선 1번, 대각선 2번, ..., 대각선 n-1번

#### 최적 이진검색트리의 재귀관계식 구하기
# 트리k: 키 Kk가 루트노드에 있는 최적이진검색트리
# 키 비교횟수: 서브트리의 비교횟수에 루트에서 비교 한 번 추가
# m!=k 인 Kk에 대해 트리k에 Km을 놓기 위한 비교 한 번 추가
#   Km의 평균검색비용에 pm을 추가
#   A[1][k-1]+A[k+1][n]+p1+p2+...+pn
# 최적 트리: k개의 트리 중 평균검색비용이 가장 작은 트리
#   A[1][n]=minimum(A[1][k-1]+A[k+1][n]+p1+....+pn)
# A[i][i]=pi
# A[i][i-1]=0
# A[j+1][j]=0
# A[i][j]=minimum(A[1][k-1]+A[k+1][n])+p1+....+pn,i<j

def optsearchtree(p):
    n=len(p)-1
    A = [[-1] * (n + 1) for _ in range(n + 2)]
    R = [[-1] * (n + 1) for _ in range(n + 2)]
    for i in range(1, n + 1):##1~n
        A[i][i - 1] = 0
        A[i][i] = p[i]##주대각선을 pi로
        R[i][i - 1] = 0
        R[i][i] = i
    A[n + 1][n] = 0
    R[n + 1][n] = 0
    for diagonal in range(1, n):##1~n-1
           for i in range(1, n - diagonal + 1):##1~n-diagonal
               j = i + diagonal
               A[i][j], R[i][j] = minimum(A, p, i, j)
    return A, R
def minimum (A, p, i, j):
    minValue = INF
    minK = 0
    for k in range(i, j + 1):
          value = A[i][k - 1] + A[k + 1][j]
          for m in range(i, j + 1):
              value += p[m]
          if (minValue > value):
              minValue = value
              minK = k
    return minValue, minK
INF = 999
keys = [0, 10, 20, 30, 40, 50]
p = [0, 35, 12, 22, 8, 15]
A, R = optsearchtree(p)
print('A = ')
for i in range(1, len(A)):
    print(A[i])##최적검색비용
print('R = ')
for i in range(1, len(R)):
    print(R[i])##최적트리의 루트노드 인덱스
####최적이진검색트리 구하기
# R[i][j]:i~j까지 최적트리의 루트노드 인덱스 ->재귀호출을 통한 분할정복
def tree (R, i, j): 
    k = R[i][j]
    if (k == 0):
        return None
    else:
        node = BSTNode(keys[k]) 
        node.left = tree(R, i, k - 1) 
        node.right = tree(R, k + 1, j) 
        return node
class BSTNode:
    def __init__ (self, key):
        self.key = key 
        self.left = None 
        self.right = None
def preorder (node):
    if (node is None):
        return
    else:
        print(node.key, end = ' ') 
        preorder(node.left) 
        preorder(node.right)
def inorder (node):
    if (node is None):
        return
    else:
        inorder(node.left) 
        print(node.key, end = ' ') 
        inorder(node.right)
root = tree(R, 1, len(p) - 1) 
print('inorder: ', end = ' ') 
inorder(root) 
print('\npreorder: ', end = ' ') 
preorder(root)

