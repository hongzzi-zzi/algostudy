def exchange(S):
    n=len(S)
    for i in range(n-1):##1~n-2까지(range(n):1~n-1까지!!)
        for j in range(i+1,n):##i+1~n-1까지(range(a,b):a~b-1까지!!)
            if(S[i]>S[j]):
                S[i],S[j]=S[j],S[i]##swap
    return S

S=[-1,10,7,11,5,13,8]
print(exchange(S))
