def location(S,low,high):##S가 정렬된 경우
    if (low>high):
        return 0
    else:
        mid=(low+high)//2##//:몫(mid는 자연수여야함)
        if (x==S[mid]):
            return mid
        elif (x<S[mid]):
            return location(S,low,mid-1)##x가 왼쪽이면(작으면) high 바꾸기(재귀)
        else:
            return location(S,mid+1,high)##x가 오른쪽이면(크면) low 바꾸기(재귀)

S=[-1,10,12,13,14,18,20,25,27,30,35,40,45]##sorted
x=18
n=len(S)-1##1-n까지. 0번째는 -1이라 의미없음
loc=location(S,1,len(S)-1)
print(loc)