def bin(n,k):##nCk   ->Divide&Conquer   ->top-down(시간복잡도:세타(nCk):지수적)
    if(k==0 or n==k):
        return 1
    else:
        return bin(n-1,k-1)+bin(n-1,k)##nCk = n-1Ck-1 + n-1Ck///top-down

def bin2(n,k):##nCk   ->Dynamic Programming(파스칼의삼각형)   ->bottom-up(시간복잡도:세타(nk):2차)
    B=[[0]*(k+1)for _ in range(n+1)]##[[0,0,...,0(k+1개)],...,[0,0,...,0]([]이 n+1개)]   ->가로 k 세로 n   ->2차원리스트
    for i in range(n+1):##0~n
        for j in range(min(i,k)+1):##0~i/k 중 작은것(파스칼의 삼각형 대칭이라서 뒷부분 계산 불필요)
            if(j==0 or j==i):##iC0=1, iCi=1
                B[i][j]=1
            else:
                B[i][j]=B[i-1][j-1]+B[i-1][j]##iCj = i-1Cj-1 + i-1Cj///bottom-up(i=0,j=1부터 시작함)
    return B[n][k]

def bin3(n,k):##nCk   ->bin2 변형   ->nCk=nCn-k(성질a), 1차원리스트만으로 구현(성질b)
    if(k>n//2):##k>n/2인 경우(성질a)
        k=n-k
    B=[0]*(k+1)##[0,0,....,0(k+1개)]   ->1차원 리스트(성질b)
    B[0]=1
    #####이부분이 이해가안대요!!!!!!!! 내가 생각한게 맞냐,,?
    for i in range(1,n+1):##1~n   ->n번 반복   ->ex)l번째 반복일 때 lC0,lC1,lC2,....lCl 한 줄(1차원리스트) 구현 ->n번째 반복 시 nC0,...nCn 한 줄 구현
        j=min(i,k)##i, k중 작은 것   ->파스칼의 삼각형 대칭이라서 뒷부분 계산 불필요...?
        while (j>0):##j가 양수인동안-->B[0]=1이고, B[1],B[2],...구현해야댐
            B[j]=B[j]+B[j-1]##뒤에서부터 계산. iCj = i-1Cj-1 + i-1Cj///bottom-up과 같음(->l번째 반복인 경우 기존의 B는 l-1C0,...l-1Cl-1 한 줄 일 것임.)
            j-=1##j 1씩 줄이며 한 줄 구현
    return B[k]##nCk리턴

# for n in range(10):##0~9
#     for k in range(n+1):##0~n
#         print(bin(n,k),end='')
#     print()
# for n in range(10):##0~9
#     for k in range(n+1):##0~n
#         print(bin2(n,k),end='')
#     print()
# for n in range(10):##0~9
#     for k in range(n+1):##0~n
#         print(bin3(n,k),end='')
#     print()