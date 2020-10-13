d=[0,0,1,-1];D=[1,-1,0,0]
n,m=map(int,input().split())
c=[[[0]*2 for _ in range(m+1)]for _ in range(n+1)] # visit 리스트
b=[[int(i)for i in input()]for _ in range(n)] # 이동할 맵

q=[];ret=-1
q+=[(0,0,1,1)] # y좌표, x좌표, 출발점부터 거리, 벽을 부술수 있는 횟수
c[0][0][1]=1 # 출발점을 visit에 표시
while q:
    y,x,l,k=q.pop(0)
    if y==n-1 and x==m-1: #꺼낸 좌표가 도착지인 경우
    	ret=l # 결과값에 그동안 이동한 거리를 넣고 break
    	break
    for i in range(4):
        Y=y+D[i] #델타을 이용 이동할 좌표의 위치를 최신화
        X=x+d[i]
        if 0<=X<m and 0<=Y<n: # 이동할 좌표가 맵 안에 있고
            if b[Y][X] and k: #벽이 있는데 벽을 부술수 있는 횟수가 1이면
                q.append((Y,X,l+1,0)) #큐에 새로운 좌표, 이동거리, 벽을 부술수 있는 잔여 횟수를 넣어준다
                c[Y][X][0]=1 #visit에는 벽을 부술수 있는 횟수가 0이므로 0인 경우에 표시
            elif b[Y][X]==0 and c[Y][X][k]==0: # 벽이 없는 경우
                q+=[(Y,X,l+1,k)] #벽이 없으면 부술수 있는지는 중요치 않으므로 k 값을 그대로 큐에 넣어준다
                c[Y][X][k]=1 # visit도 마찬가지로 k값을 그대로 한채로 표시
print(ret)