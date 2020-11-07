from collections import deque
p={1:[(1,0),(0,1),(-1,0),(0,-1)],2:[(1,0),(-1,0)],3:[(0,1),(0,-1)],4:[(-1,0),(0,1)],5:[(1,0),(0,1)],6:[(1,0),(0,-1)],7:[(-1,0),(0,-1)]}
for t in range(int(input())):
    n,m,r,c,l=map(int,input().split());b=[[*map(int,input().split())]for _ in range(n)];q=deque([(r,c)]);v=[[0]*m for _ in range(n)];v[r][c]=1;cnt=1
    while q:
        y,x=q.popleft()
        for dy,dx in p[b[y][x]]:
            ny,nx=y+dy,x+dx
            if 0<=nx<m and 0<=ny<n and b[ny][nx] and (-dy,-dx) in p[b[ny][nx]] and v[ny][nx]==0:
                v[ny][nx]=v[y][x]+1;q.append((ny,nx))
                if v[ny][nx]<=l:cnt+=1
    print(f'#{t+1}',cnt)