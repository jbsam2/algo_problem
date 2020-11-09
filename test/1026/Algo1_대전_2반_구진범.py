for t in range(int(input())):
    n,c,x,y,k,r=map(int,input().split());ret=0 # 필요한 값들을 입력 받는다.
    b=[[*map(int,input().split())]for _ in range(n)] # 먼저 기본이 되는 사각 영역을 입력 받는다.
    c=(c//90)%4;x-=1;y-=1;r-=1 # 입력 받은 값중 인덱스 값을 1씩 줄여서 언어의 기본 인덱스와 맞추어 주고 회전시키는 값은 90도 회전을 몇번 시키는가로 바꾸어 준다.
    if x+k>=n or y+k>=n:ret=-1 # 만약 부분 사각형이 인덱스 범위 밖이면 -1을 출력 시킬 준비를 한다.
    if ret!=-1: #만약 부분사각형이 인덱스 범위 안이라면
        tmp=[b[y+i][x:x+k]for i in range(k)] # 부분 사각형을 잘라서 임시 저장을 한다.
        for i in range(c):tmp=[*zip(*tmp[::-1])] # 부분 사각형을 아까 바꾸어준 횟수만큼 90도 회전을 시킨다.
        for i in range(k):
            for j in range(k):
                b[y+i][x+j]=tmp[i][j] # 회전시킨 부분 사각형을 다시 원래 영역에 넣어준다.
    print(f'#{t+1}',sum(b[r])if ret!=-1 else -1) # 계산한 값을 출력시켜준다.