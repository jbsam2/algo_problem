def sol(t,p):
    global c
    if t>k:return
    if t==k:c+=1;return
    if p>n-1:return
    sol(t,p+1);sol(t+a[p],p+1)
for t in range(int(input())):
    global n,k,a
    c=0;n,k=map(int,input().split());a=list(map(int,input().split()));sol(0,0);print(f'#{t+1}',c)