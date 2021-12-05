def matrixmul(A,B):##먼개소린지 모르게써용!
    n=len(A)
    C=[[0]*n for _ in range(n)]##먼개소리노...
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]##이건또 뭐노,,,cij=시그마(k=1~n)aik*bkj....
    return C

A=[[2,3],[4,1]]
B=[[5,7],[6,8]]##왜 56/78 이 아닌걸까요 tlqkf 아 Bkj라서..? 아닌가? 몰라 행렬 시렁ㅠㅠ
print(matrixmul(A,B))