for t in range(int(input())):
    n,m=map(int,input().split()) # 사이즈를 입력
    b=[[*map(int,input().split())]for _ in range(n)] #초기 적군 배치를 입력
    ret=set() # 폭탄이 영향을 끼치는 좌표를 저장할 set
    ans=0 # 처치한 적군의 수를 저장할 변수
    for _ in range(m): #폭탄의 갯수만큼 반복
        y,x,r=map(int,input().split()) #폭탄의 정보를 입력 받는다.
        ret.add((y,x)) #폭탄이 떨어진 위치를 ret에 저장
        for i in range(1,r+1): # r 범위 만큼 탐색 시작
            ny1=y-i # r만큼 위쪽으로 탐색
            ny2=y+i # 아래쪽 탐색
            nx1=x-i # 왼쪽 탐색
            nx2=x+i # 오른쪽 탐색
            if 0<=ny1<n:ret.add((ny1,x)) # 각각의 탐색 범위가 지도 안에 있다면 해당 좌표를 ret에 저장
            if 0<=ny2<n:ret.add((ny2,x))
            if 0<=nx1<n:ret.add((y,nx1))
            if 0<=nx2<n:ret.add((y,nx2))
    for i in ret:
        ans+=b[i[0]][i[1]] # ret에 저장된 좌표를 돌면서 해당 위치에 있는 적군의 수를 더해준다.
    print(f'#{t+1}',ans)