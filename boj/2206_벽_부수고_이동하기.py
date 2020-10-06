d=[0,0,1,-1];D=[1,-1,0,0]
n,m=map(int,input().split())
c=[[[0]*2 for _ in range(m+1)]for _ in range(n+1)]
b=[[int(i)for i in input()]for _ in range(n)]
q=[];ret=-1
q+=[(0,0,1,1)]
c[0][0][1]=1
while q:
    y,x,l,k=q.pop(0)
    if y==n-1 and x==m-1:ret=l;break
    for i in range(4):
        Y=y+D[i];X=x+d[i]
        if 0<=X<m and 0<=Y<n:
            if b[Y][X] and k:
                q.append((Y,X,l+1,0))
                c[Y][X][0]=1
            elif b[Y][X]==0 and c[Y][X][k]==0:
                q+=[(Y,X,l+1,k)]
                c[Y][X][k]=1
print(ret)