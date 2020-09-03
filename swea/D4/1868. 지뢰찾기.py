d=[1,-1,0]
def sol(y,x):
    global r
    c=0
    for i in d:
        for j in d:
            if b[i+y][j+x]=='.':c+=1
    if c==9:
        q.append((y,x))
        v[y][x]=1
        while q:
            c=0;f,e=q.pop(0)
            for i in d:
                for j in d:
                    if b[i+f][j+e]=='.':c+=1
            if c==9:
                for i in d:
                    for j in d:
                        if v[i+f][j+e]==0 and 0<i+f<=n and 0<j+e<=n:q.append((i+f,j+e));v[i+f][j+e]=1
        r+=1

for t in range(int(input())):
    n=int(input());b=[[*'.'*(n+2)]]+[[*'.'+input()+'.'] for _ in range(n)]+[[*'.'*(n+2)]];a=0;q=[];r=0;v=[[0]*(n+2)for _ in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if v[i][j]==0:sol(i,j)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if v[i][j]==0 and b[i][j]=='.':r+=1
    print('#{}'.format(t+1),r)

########################################################################################################################################################

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
            if b[i][j]=='.':
                a+=1
    print('#{}'.format(t+1),a)