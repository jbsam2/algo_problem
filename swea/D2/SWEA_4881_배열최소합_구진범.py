'''def sol(k,u,s):
    global a
    if s>=a:return
    if k==len(l):a=min(a,s);return
    for i in range(len(l)):
        if u&1<<i:continue
        sol(k+1,u|1<<i,s+l[k][i])
for t in range(int(input())):l=[[*map(int,input().split())]for _ in range(int(input()))];a=1<<32;sol(0,0,0);print(f'#{t+1}',a)'''
def sol(r):
    global a,s
    if s>=a:return
    if r==len(l):a=min(a,s);return
    for i in range(len(l)):
        if i not in v:v.append(i);s+=l[r][i];sol(r+1);s-=l[r][i];v.remove(i)        
for t in range(int(input())):l=[[*map(int,input().split())]for _ in range(int(input()))];a=1<<32;v=[];s=0;sol(0);print(f'#{t+1}',a)