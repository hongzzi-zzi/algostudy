def quicksort(S,low,high):##책에나온방법
    if (high>low):
        pivotpoint=partition(S,low,high)##pivotpoint는 어케정하노?->편의상 일단 리스트의 첫 원소로 ㅇㅇ
        quicksort(S,low,pivotpoint-1)##mid-1(왼쪽 재귀호출)
        quicksort(S,pivotpoint+1,high)##mid+1(오른쪽 재귀호출)
def partition(S,low,high):
    pivotitem=S[low]
    j=low
    for i in range(low+1,high+1):##low+1~high까지
        if(S[i]<pivotitem):##S[i]가 S[low]보다 작으면
            j+=1#j하나 키우기
            S[i],S[j]=S[j],S[i]##swap
    pivotpoint=j
    S[low],S[pivotpoint]=S[pivotpoint],S[low]##swap         S[low],S[j]=S[j],S[low] 한거
    return pivotpoint##j리턴한거랑 똑같음


def quicksort2(S,low,high):
    if (high>low):
        pivotpoint=partition2(S,low,high)##pivotpoint는 어케정하노?->편의상 일단 리스트의 첫 원소로 ㅇㅇ
        # print(S)
        # print(pivotpoint)
        quicksort2(S,low,pivotpoint-1)##mid-1(왼쪽 재귀호출)
        quicksort2(S,pivotpoint+1,high)##mid+1(오른쪽 재귀호출)
def partition2(S,low,high):
    pivotitem=S[low]
    i=low+1
    j=high##pivotitem,i,j 설정

    while(i<=j):
        while(S[i]<pivotitem):
            i+=1##S[i]가 pivotitem보다 작은동안 i 1씩 증가
            if i>len(S)-1: break##예외처리,,,리스트인덱스에러나서!
        while(S[j]>pivotitem):
            j-=1###S[j]가 pivotitem보다 큰동안 j 1씩 감소
            if j<0:break
        if(i<j):##i, j 역전되기 전(같아지기 전)
            S[i],S[j]=S[j],S[i]##swap
    pivotpoint=j
    S[low],S[pivotpoint]=S[pivotpoint],S[low]##swap         S[low],S[j]=S[j],S[low] 한거
    return pivotpoint##j리턴한거랑 똑같음

S=[15,22,13,27,12,10,20,25]
quicksort2(S,0,len(S)-1)
print(S)
