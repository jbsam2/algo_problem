n=int(input())
b=[[*map(int,input().split())]for _ in range(n)]
ans=[0]*3
def sol(x,y,s):
    global ans
    if s==1:ans[b[y][x]+1]+=1;return
    m=z=p=1
    for i in range(y,y+s):
        for j in range(x,x+s):
            if b[i][j]==-1:z=p=0
            elif b[i][j]==0:m=p=0
            else:m=z=0
    if m:ans[0]+=1
    elif z:ans[1]+=1
    elif p:ans[2]+=1
    else:
        d=s//3
        for i in range(3):
            for j in range(3):sol(x+i*d,y+j*d,d)
sol(0,0,n)
print(*ans,sep='\n')



'''
n=int(input())
p=[[*map(int,input().split())]for _ in range(n)]
ans=[0]*3
def sol(x,y,s):
    if s==1:return p[y][x]
    r=[]
    for i in range(y,y+s,s//3):
        for j in range(x,x+s,s//3):r.append(sol(i,j,s//3))
    if len(set(r))==1 and r[0]!=None:return r[0]
    for i in r:
        if i==None:continue
        ans[1+i]+=1
    return None
t=sol(0,0,n)
if t!=None:ans[1+t]+=1
print(*ans,sep='\n')
'''