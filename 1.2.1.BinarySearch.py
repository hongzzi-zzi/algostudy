def binsearch(n,S,x):
    low=1
    high=n
    location=0
    cnt=1
    while (low<=high and location==0):
        mid=(low+high)//2 ##//:몫, 매번 새로운 mid 생김!!
        if x==S[mid]:
            location=mid
        elif S[mid]>x:
            high=mid-1##왼쪽 재귀호출
        else:
            low=mid+1##오른쪽 재귀호출
        cnt+=1
    return location
S=[-1,5,7,8,10,11,13]##sorted
n=len(S)-1
x1=2##0(리스트에 없음)
x2=7##2
x3=13##6
print(binsearch(n,S,x1))
print(binsearch(n,S,x2))
print(binsearch(n,S,x3))