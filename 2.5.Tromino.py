def tromino(board,srow,scol,size,xrow,xcol):
    if size==1:
        return
    else:##divide
        ####    1|2
        ####    3|4 사분면
        mrow=srow+(size//2)
        mcol=scol+(size//2)
        xrow1,xcol1=mrow-1,mcol-1
        xrow2,xcol2=mrow-1,mcol
        xrow3,xcol3=mrow,mcol-1
        xrow4,xcol4=mrow,mcol

        if(xrow<mrow and xcol<mcol):##1사분면
            fillCenterExcept(board,mrow,mcol,1)##fillCenterExcept 함수 정의(중심빼고 채우는거)
            xrow1,xcol1=xrow,xcol
        elif(xrow<mrow and xcol>=mcol):##2사분면
            fillCenterExcept(board,mrow,mcol,2)##fillCenterExcept 함수 정의(중심빼고 채우는거)
            xrow2,xcol2=xrow,xcol
        elif(xrow>=mrow and xcol<mcol):##3사분면
            fillCenterExcept(board,mrow,mcol,3)##fillCenterExcept 함수 정의(중심빼고 채우는거)
            xrow3,xcol3=xrow,xcol
        elif(xrow>=mrow and xcol>=mcol):##4사분면
            fillCenterExcept(board,mrow,mcol,4)##fillCenterExcept 함수 정의(중심빼고 채우는거)
            xrow4,xcol4=xrow,xcol
        ###conquer(재귀)
        tromino(board,srow,scol,size//2,xrow1,xcol1)##1사분면
        tromino(board,srow,mcol,size//2,xrow2,xcol2)##2
        tromino(board,mrow,scol,size//2,xrow3,xcol3)##3
        tromino(board,mrow,mcol,size//2,xrow4,xcol4)##4

def fillCenterExcept(board,mrow,mcol,part):##중심빼고 채우는 함수
    global tromino_cnt##전역변수로 트로미노갯수 잡아줌
    tromino_cnt+=1##한번부를때마다 1식 더해줌
    if (part!=1):##1사분면이 아닌 경우
        board[mrow-1][mcol-1]=tromino_cnt
    if (part!=2):##2사분면이 아닌 경우
        board[mrow-1][mcol]=tromino_cnt
    if (part!=3):##3사분면이 아닌 경우
        board[mrow][mcol-1]=tromino_cnt
    if (part!=4):##4사분면이 아닌 경우
        board[mrow][mcol]=tromino_cnt

def print_board(board):##출력
    for i in range(m):##1~m-1
        for j in range(m):
            if board[i][j]<0:
                print("%3s"%"X",end='')
            else:
                print("%3d"%board[i][j],end='')
        print()

import random##random함수 사용
m=8##m=2^k 꼴
xrow=random.randint(0,m-1)
xcol=random.randint(0,m-1)
print(xrow,xcol)
board=[[0]*m for _ in range(m)]#m*m행렬
board[xrow][xcol]=-1
tromino_cnt=0
tromino(board,0,0,m,xrow,xcol)
print_board(board)