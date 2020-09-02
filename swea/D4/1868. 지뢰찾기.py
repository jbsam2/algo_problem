d=[1,-1,0]
def s(y,x):
    for i in d:
        for j in d:
            nx=x+j;ny=y+i
            if not i==j==0 and -1<nx<n and -1<ny<n and b[ny][nx]=='*':b[y][x]=1;return
    b[y][x]=1
    for i in d:
        for j in d:
            nx=x+j;ny=y+i
            if not i==j==0 and -1<nx<n and -1<ny<n and b[ny][nx]!=1:s(ny,nx)
def c(y,x):
    for i in d:
        for j in d:
            nx=x+j;ny=y+i
            if not i==j==0 and -1<nx<n and -1<ny<n and b[ny][nx]=='*':return 1
    return 0
for t in range(int(input())):
    n=int(input());b=[[*input()]for _ in range(n)];a=0;v=[]
    for i in range(n):
        for j in range(n):
            if b[i][j]=='.':
                if c(i,j)==0:s(i,j);a+=1
    for i in range(n):
        for j in range(n):
            if b[i][j]=='.':a+=1
    print('#{}'.format(t+1),a)