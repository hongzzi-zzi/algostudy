###정렬 ㄴㄴ
def mergesort(S):
    n=len(S)
    if n<=1:
        return S##원소 1개인경우 그대로 리턴
    else:
        mid=n//2##몫
        ##분할
        U=mergesort(S[0:mid])##슬라이싱(s1)->S[0]~S[mid-1]
        V=mergesort(S[mid:n])##슬라이싱(s2)->S[mid]~S[n-1]
        return merge(U,V)##합병
def merge(U,V):
    S=[]##새로운 리스트
    i=0
    j=0##인덱스
    while(i<len(U)and j<len(V)):
        if U[i]>V[j]:
            S.append(V[j])#V[j]가 작으면 작은거 S에 append
            j+=1##j++
        else:##그 반대
            S.append(U[i])
            i+=1
    if(i<len(U)):
        S+=U[i:len(U)]##j>len[V]->V는 다끝나면 남은 U를 S 뒤에 붙이기(U[i]~U[len(U)-1])
    else:
        S+=V[j:len(V)]##그 반대
    return S
S=[27,10,12,20,25,13,15,22]##unsorted
print(mergesort(S))