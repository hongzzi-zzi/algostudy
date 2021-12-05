def sum(n,S):
    result=0
    for i in range(1,n+1):#1부터 n까지 더하기
        result+=S[i]
    return result

S=[-1,10,7,11,5,13,8]
n=len(S)-1
print(sum(n,S))

