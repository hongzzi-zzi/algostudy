def ladd(u,v):##큰 수의 덧셈
    n=len(u) if(len(u)>len(v)) else len(v)##max(len(u),len(v))
    result=[]
    carry=0

    for k in range(n):#0~n-1까지
        i=u[k] if(k<len(u)) else 0
        j=v[k] if(k<len(v)) else 0
        val=i+j+carry
        carry=val//10##10으로 나눈 몫
        result.append(val%10)##10으로 나눈 나머지 (자리수맞는거) result에 append
   
    if(carry>0):##마지막에 carry가 0보다 크면
        result.append(carry)##마지막에 올림수
    
    return result

# u=[6,7,8,9]##9876
# v=[3,4,5]##543
# print(ladd(u,v)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)

# u=[2,3,8,7,6,5]##567832
# v=[3,2,7,3,2,4,9]##9423723
# print(ladd(u,v)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)


def prod(u,v):##곱셈:분할 정복(재귀4->효율적이지않음)
    n=len(u) if(len(u)>len(v)) else len(v)##max(len(u),len(v))

    if(len(u)==0 or len(v)==0):##둘 중 하나라도 0이면(길이 0)
        return [0]##[0] 리턴
    elif(n<=threshold):
        return lmult(u,v)##lmult(큰 수 곱셈 정의해주기)
    else:
        # u=x*10^m+y
        # v=w*10^m+z
        # uv=(x*10^m+y)*(w*10^m+z)=xw*10^2m+(xz+yw)*10^m+yz
        # p1=xw,p2=xz+yw,p3=yz
        # 이 식 사용함 ㅇㅇ
        m=n//2##자연수여야함->몫(//)사용
        ##분할
        x=div(u,m);y=rem(u,m)##x:몫/y:나머지(div,rem 정의해주기)
        w=div(v,m);z=rem(v,m)##w:몫/z:나머지
        ##정복
        p1=prod(x,w)
        p2=ladd(prod(x,z),prod(w,y))
        p3=prod(y,z)##재귀 4번 사용됨(prod 4번)
        return ladd(ladd(exp(p1,2*m),exp(p2,m)),p3)##공식사용, exp(지수연산) 정의해주기
    
##10의 지수 m 으로 나눈 몫: m+1의 자리에서 n의 자리까지가 몫
def div(u,m):##몫 구하는 함수(u:리스트, m:자연수)->u//10^m
    if(len(u)<m):##자리수가 m 보다 작으면
        u.append(0)
    return u[m:len(u)]##m~len(u)-1까지 슬라이싱(m+1의 자리~n의 자리)

##10의 지수 m 으로 나눈 나머지: 1의 자리에서 m의 자리까지가 나머지
def rem(u,m):##나머지 구하는 함수(u:리스트, m:자연수)->u%10^m
    if(len(u)<m):##자리수가 m 보다 작으면
        u.append(0)
    return u[0:m]##0~m까지 슬라이싱(1의 자리~m의 자리)

##10의 지수 m으로 곱하기: 왼쪽으로 m 자릿수만큼 쉬프트
def exp(u,m):##곱한것 구하는 함수(u:리스트, m:자연수)->u*10^m
    if(u==[0]):
        return[0]##0*10^m=0
    else:
        ##ex)u=[5,6,7](765)일 때,765*10^m은 [0,0,...,0(0이 m 개)]+[5,6,7]=[0,0,...,0(0이 m개),5,6,7]->7650000...0(0 m 개)
        return ([0]*m)+u

# u=[2,3,8,7,6,5]##567832
# v=[3,2,7,3,2,4,9]##9423723
# print(exp(u,3)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)
# print(div(u,3)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)
# print(rem(u,3)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)

def lmult(u,v):##큰 수의 곱셈, threshold=1인 경우(한자리수 곱셈 ,,,?)
    i=u[0] if(0<len(u)) else 0
    j=v[0] if(0<len(v)) else 0##일의자리수를 각각 i,j 로 둠
    val=i*j
    carry=val//10##올림
    result=[]
    result.append(val%10)##일의자리를 result에 append
    if(carry>0):##올림이 있는 경우
        result.append(carry)##carry 를 result에 append
    return result

# u=[8]
# v=[7]
# print(lmult(u,v)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)

# u=[2,3,8,7,6,5]##567832
# v=[3,2,7,3,2,4,9]##9423723
# threshold=1
# print(prod(u,v)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)

def prod2(u,v):##곱셈:분할 정복(재귀3->효율적)
    n=len(u) if(len(u)>len(v)) else len(v)##max(len(u),len(v))
    if(len(u)==0 or len(v)==0):##둘 중 하나라도 0이면(길이 0)
        return [0]##[0] 리턴
    elif(n<=threshold):
        return lmult(u,v)##lmult(큰 수 곱셈 정의해주기)
    else:
        # u=x*10^m+y
        # v=w*10^m+z
        # uv=(x*10^m+y)*(w*10^m+z)=xw*10^2m+(xz+yw)*10^m+yz
        # r=(x+y)(w+z)=xw+(xz+yw)+yz
        # (xz+yw)=r-(xw+yz)
        # uv=xw*10^2m+(xz+yw)*10^m+yz=xw*10^2m+(r-(xw+yz))*10^m+yz
        # 곱셈 3번으로 줄음(r,xw,yz...? 맞낭)
        m=n//2##자연수여야함->몫(//)사용
        ##분할
        x=div(u,m);y=rem(u,m)##x:몫/y:나머지(div,rem 정의해주기)
        w=div(v,m);z=rem(v,m)##w:몫/z:나머지
        #######r 새로 정의
        r=prod2(ladd(x,y),ladd(w,z))
        p1=prod2(x,w)
        p3=prod2(y,z)##prod2 3번(재귀 3번)->세타(n^log2 3)됨->효율성 up
        p2=lsub(r,ladd(p1,p3))##ladd(뺄셈) 구현
        return ladd(ladd(exp(p1,2*m),exp(p2,m)),p3)

def lsub(u,v):##큰수 뺄셈
    n=len(u) if(len(u)>len(v)) else len(v)##max(len(u),len(v))
    result=[]
    borrow=0##음...?
    
    for k in range(n):##0~n-1까지
        i=u[k] if(k<len(u)) else 0
        j=v[k] if(k<len(v)) else 0
        val=i-j+borrow
        if(val<0):
            val+=10
            borrow=-1
        else:
            borrow=0
        result.append(val%10)
    if(borrow<0):
        print('음의 정수는 처리 못 함')
    return result

u=[2,3,8,7,6,5]##567832
v=[3,2,7,3,2,4,9]##9423723
threshold=1
print(prod(u,v)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)
# print('a')
print(prod2(u,v)[::-1])##리스트 슬라이싱(전체를 거꾸로 출력)