import sys
b=[list(map(int,sys.stdin.readline().split()))for _ in range(9)]
row=[[0]*10 for _ in range(9)]
col=[[0]*10 for _ in range(9)]
square=[[0]*10 for _ in range(9)]
get=[[i//3*3+j//3 for j in range(9)]for i in range(9)]
z=[]
for i in range(9):
    for j in range(9):
        if b[i][j]==0:
            z.append((i,j))
        else:
            row[i][b[i][j]]=1
            col[j][b[i][j]]=1
            square[get[i][j]][b[i][j]]=1
def sol(c):
    if len(z)==c:
        [print(*b[i])for i in range(9)]
        sys.exit()
    i,j=z[c]
    for k in range(1,10):
        if row[i][k] or col[j][k] or square[get[i][j]][k]:continue
        b[i][j]=k
        row[i][k]=col[j][k]=square[get[i][j]][k]=1
        sol(c+1)
        row[i][k]=col[j][k]=square[get[i][j]][k]=0
sol(0)