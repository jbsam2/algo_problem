for t in range(int(input())):
    ret=0 # 최종 결과를 저장할 변수
    n,m=map(int,input().split()) #n,m 입력
    s=sorted([(j,i) for i,j in enumerate([*map(int,input().split())])]) #돌의 크기를 인덱스와 함께 저장후 돌의 크기를 기준으로 오름차순 정렬을 한다.
    jump_idx=[];jumps=n-m;s_idx=0 #jump_idx: 건너뛸 돌의 인덱스, jumps: 건너뛰어야 하는 돌의 갯수, s_idx: 저장한 s list의 인덱스
    if jumps==0:ret=sum([s[i][0]for i in range(n)]) #만약에 건너뛰어야하는 돌이 없다면 전부다 밟는다.
    else:
        while jumps: # 뛰어넘어야하는 돌의 갯수가 남아있는 동안
            stone_idx=s[s_idx][1] # 돌의 인덱스 값을 불러온다.
            if stone_idx+1 in jump_idx or stone_idx-1 in jump_idx: # 만약에 현재 고른 돌의 앞뒤 돌중 하나라도 이미 뛰어 넘었다면
                s_idx+=1 #s에서 다음으로 작은 크기의 돌을 불러온다.
            else: #현재 돌을 뛰어넘을수 있다.
                jump_idx.append(stone_idx) #뛰어넘은 돌의 인덱스를 저장
                s_idx+=1 # 다음으로 작은 크기의 돌을 불러온다.
                jumps-=1 # 점프 가능 횟수를 하나 줄인다.
        ret=sum(s[i][0] for i in range(n) if s[i][1] not in jump_idx) # 뛰어넘은 돌을 제외한 나머지 돌들의 크기를 더한다.
    print(f'#{t+1}',ret)