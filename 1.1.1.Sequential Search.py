def seqsearchsource(n,S,x):
    location=1
    while(location<=n and S[location]!=x):
        location+=1
    if(location>n):
        location=0
    return location


def seqsearch(n,S,x):##내코드
    for i in range(0,n):
        if S[i]==x:
            return i
    return 0
S=[0,10,7,11,5,13,8]
x=5
n=len(S)-1
print(seqsearch(n,S,x))
print(seqsearchsource(n,S,x))
x=4
print(seqsearch(n,S,x))
print(seqsearchsource(n,S,x))