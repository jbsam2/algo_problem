def sol(pos):
    global cnt,ret
    if pos>=n:ret=min(ret,cnt);return
    if cnt>ret:return
    for i in range(pos+b[pos],pos,-1):cnt+=1;sol(i);cnt-=1
for t in range(int(input())):b=[*map(int,input().split())];n=b[0];ret=1<<32;cnt=0;sol(1);print(f'#{t+1}',ret-1)