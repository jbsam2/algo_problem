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