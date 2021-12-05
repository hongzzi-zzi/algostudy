# Greedy Approach
# 1. 초기화: 해답집합을 공집합으로 둠
# -> 간선 집합 E의 부분집합 F를 공집합으로 둠
# 2. 선택: 최적의 원소 하나를 해답의 집합에 포함시킴
# -> E에서 최적의 간선 하나를 추출해서 F에 포함시킴 ->프림/크루스칼
# 3. 검사: 해답의 집합이 최종이면 종료 / 아니면 2 반복
# -> 간선의 부분집합 F의 원소갯수가 n-1이면 최종해답

#### 크루스칼 알고리즘
# 1. 해답의 집합을 공집합으로 둠. F=공집합
#    V의 서로소집합(disjoint union)생성
#    E를 비내림차순으로 정렬
# 2. 최적의 원소 하나를 해답의 집합에 포함시킴
#    정렬된 E집합에서 간선 e=(i,j)선택
#    두 정점 i, j가 속한 집합 p, q를 찾아서
#    p=q: e를 버림 -> Find
#    p!=q: F에 e를 포함한 후, p, q를 합친다 -> Union
# 3. |F|=n-1이면 종료, 아니면 2단계 반복

####사이클 탐지 how?
# 서로소집합: 교집합이 공집합인 두 집합 A, B는 서로소집합
# Union find algo: 서로소집합 자료구조를 이용, 두 개의 원소가 같은 집합에 속하는지 판단할 수 있는 알고리즘

class DisjointSet:
    def __init__ (self, n):
        self.U = []
        for i in range(n):
            self.U.append(i)
    def equal (self, p, q): 
        if (p == q):
           return True
        else:
           return False
    def find (self, i): 
        j=i
        while (self.U[j] != j):
            j = self.U[j]
        return j
    def union (self, p, q):
        if (p < q):
            self.U[q] = p
        else:
            self.U[p] = q
    
def kruskal(n,E):
    F=[]
    dset=DisjointSet(n)
    while (len(F) < n - 1):
          edge = E.pop(0)
          i, j = edge[0], edge[1]
          p = dset.find(i)
          q = dset.find(j)
          if (not dset.equal(p, q)):
              dset.union(p, q)
              F.append(edge)
    return F
def cost (F):
    total = 0
    for e in F:
        total += e[2]
    return total
INF = 999 
n=5 
E=[[0, 1, 1],[2, 4, 2],[0, 2, 3],[1, 2, 3], [2, 3, 4],[3, 4, 5], [1, 3, 6]]
F = kruskal(n, E)
for i in range(len(F)):
    print(F[i])
print(cost(F))