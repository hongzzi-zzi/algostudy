def fibRec(n):##재귀
    if n<=1:
        return n
    else:
        return fibRec(n-2)+fibRec(n-1)##fibRec(n)
def fibIte(n):##반복
    f=[0]*(n+1)##[0,0,....,0](0 이 총 n-1개)->f[0]=0,f[1]=0,......
    if n>0:
        f[1]=1
        for i in range(2,n+1):##2~n까지
            f[i]=f[i-2]+f[i-1]
    return f[n]
def fibNoList(n):##리스트안씀
    f0=0
    f1=1
    result=0
    if n==0:
        result=0
    elif n==1:
        result=1
    else:##n>1
        for i in range(2,n+1):#2~n까지
            result=f0+f1
            f0=f1
            f1=result
    return result

for i in range(11):##0~10까지
    print(fibRec(i),end=' ')
print('')
for i in range(11):##0~10까지
    print(fibIte(i),end=' ')
print('')
for i in range(11):##0~10까지
    print(fibNoList(i),end=' ')
print('')
