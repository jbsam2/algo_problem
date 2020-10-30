for t in range(int(input())):
    n=int(input());m=1<<n;d=[0]*m;p=[[*map(lambda x:x*.01,map(int,input().split()))]for _ in range(n)];d[0]=1
    for i in range(m):
        x=bin(i).count('1')
        for j in range(n):
            if(1<<j)&i==0:d[i|(1<<j)]=max(d[i|(1<<j)],d[i]*p[x][j])
    print(f'#{t+1} {d[-1]*100:.6f}')

def sol(r,s):
    global a
    if s<=a:return
    if r==len(l):a=max(a,s);return
    for i in range(len(l)):
        if i not in v:v.append(i);sol(r+1,s*l[r][i]);v.remove(i)        
for t in range(int(input())):l=[[*map(lambda x:x*.01,map(int,input().split()))]for _ in range(int(input()))];a=0;v=[];sol(0,1);print(f'#{t+1} {a*100:.6f}')