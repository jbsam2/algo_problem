for t in range(int(input())):
    n=int(input())
    b=[[0]*n for i in range(n)]
    dy=[0,1,0,-1]
    dx=[1,0,-1,0]
    direction=row=col=0
    number=1
    while number<=n*n:
        b[row][col]=number
        number+=1
        new_row=row+dy[direction]
        new_col=col+dx[direction]
        if 0<=new_row<n and 0<=new_col<n and b[new_row][new_col]==0:
            row,col=new_row,new_col
        else:
            direction=(direction+1)%4
            row+=dy[direction]
            col+=dx[direction]

    print(f'#{t+1}')
    for i in range(n):
        for j in range(n):print(b[i][j],end=' ')
        print()
###################################################################################################

for t in range(int(input())):
    n=int(input());b=[[0]*n for _ in range(n)];l=1;dx=[1,0,-1,0];dy=[0,1,0,-1];r=c=d=0
    while l<=n*n:
        b[r][c]=l;nr=r+dy[d];nc=c+dx[d];l+=1
        if 0<=nr<n and 0<=nc<n and b[nr][nc]==0:r,c=nr,nc
        else:d=(d+1)%4;r+=dy[d];c+=dx[d]
    print('#{}'.format(t+1))
    for i in b:print(*i)