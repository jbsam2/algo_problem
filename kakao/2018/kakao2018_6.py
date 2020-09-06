def solution(m, n, board):
    x=[[*i] for i in board];flag=1
    while flag:
        a=[];flag=0
        for i in range(m-1):
            for j in range(n-1):
                if x[i][j]==x[i][j+1]==x[i+1][j]==x[i+1][j+1]!=1:a.append([i,j]);flag=1
        for k in a:
            i,j=k[0],k[1]
            x[i][j],x[i][j+1],x[i+1][j],x[i+1][j+1]=1,1,1,1
        for j in range(n):
            for k in range(m):
                for i in range(m-1):
                    if x[i+1][j]==1:x[i+1][j],x[i][j]=x[i][j],1
    return sum(x,[]).count(1)