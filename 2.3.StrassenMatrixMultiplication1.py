def strassen(A,B):##n*n행렬 곱 (분할 정복)
    n=len(A)
    if n<=threshold:
        return matrixmult(A,B)##간단한 경우 그냥 정의 이용해서 계산(matrixmult함수 만들기)

    A11,A12,A21,A22=divide(A)
    B11,B12,B21,B22=divide(B)## 행렬 4개로 쪼개기(divide함수 만들기)

    ###분할(재귀적으로!)
    M1=strassen(madd(A11,A22),madd(B11,B22))
    M2 = strassen(madd(A21, A22), B11)
    M3 = strassen(A11, msub(B12, B22))
    M4 = strassen(A22, msub(B21, B11))
    M5 = strassen(madd(A11, A12), B22)
    M6 = strassen(msub(A21, A11), madd(B11, B12))
    M7 = strassen(msub(A12, A22), madd(B21, B22))##madd,msub함수 만들기

    ###정복
    return conquer(M1,M2,M3,M4,M5,M6,M7)##conquer함수 만들기

def matrixmult(A,B):##algo 1.1.4
    n=len(A)
    C=[[0]*n for _ in range(n)]##[[0,0,0,....0](0이 n개),[0,0,....0],....,[0,0,....0]([]가 n 개)]n*n행렬 만들기

    for i in range(n):##0~n-1까지
        for j in range(n):
            for k in range(n):##0~n-1까지
                C[i][j]+=A[i][k]*B[k][j]
                
    return C

def divide(A):##행렬 4개로 쪼개는 함수
    n=len(A)
    m=n//2#몫(자연수여야함)
    A11=[[0]*m for _ in range(m)]##[[0,0,0,....0](0이 m개),[0,0,....0],....,[0,0,....0]([]가 m 개)]m*m행렬 만들기
    A12=[[0]*m for _ in range(m)]
    A21=[[0]*m for _ in range(m)]
    A22=[[0]*m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            A11[i][j]=A[i][j]##왼쪽 위
            A12[i][j]=A[i][j+m]##오른쪽(j+m)위
            A21[i][j]=A[i+m][j]##왼쪽 아래(i+m)
            A22[i][j]=A[i+m][j+m]##오른쪽(j+m)아래(i+m)
    return A11,A12,A21,A22##tuple로 여러개 리턴

def madd(A,B):##행렬 덧셈
    n=len(A)
    C=[[0]*n for _ in range(n)]##[[0,0,0,....0](0이 n개),[0,0,....0],....,[0,0,....0]([]가 n 개)]n*n행렬 만들기

    for i in range(n):
        for j in range(n):
            C[i][j]=A[i][j]+B[i][j]

    return C

def msub(A,B):##행렬 뺄셈
    n=len(A)
    C=[[0]*n for _ in range(n)]##[[0,0,0,....0](0이 n개),[0,0,....0],....,[0,0,....0]([]가 n 개)]n*n행렬 만들기

    for i in range(n):
        for j in range(n):
            C[i][j]=A[i][j]-B[i][j]

    return C

def conquer(M1,M2,M3,M4,M5,M6,M7):##정복

    C11=madd(msub(madd(M1,M4),M5),M7)##((M1+M4)-M5)+M7
    C12 = madd(M3, M5)
    C21 = madd(M2, M4)
    C22 = madd(msub(madd(M1, M3), M2), M6)##쉬트라쎈 공식(?) 사용

    m=len(C11)
    n=2*m
    C=[[0]*n for _ in range(n)]##[[0,0,0,....0](0이 n개),[0,0,....0],....,[0,0,....0]([]가 n 개)]n*n행렬 만들기

    for i in range(m):
        for j in range(m):
            C[i][j]=C11[i][j]
            C[i][j+m]=C12[i][j]
            C[i+m][j]=C21[i][j]
            C[i+m][j+m]=C22[i][j]##행렬 채워넣기

    return C

A=[[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
B=[[8,9,1,2],[3,4,5,6],[7,8,9,1],[2,3,4,5]]
threshold=2
C=strassen(A,B)##스트라쎈방법
D=matrixmult(A,B)##정의 이용한 방법
print(C)
print(D)
# for i in range(len(C)):
#     print('C[%d]='%(i),C[i])
# for i in range(len(D)):
#     print('D[%d]='%(i),D[i])