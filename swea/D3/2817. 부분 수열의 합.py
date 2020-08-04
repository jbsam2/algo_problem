def sol(total,pos):
    global c
    if total > k:return
    if total == k:
        c+=1
        return
    if pos > n-1:return
    sol(total,pos+1)
    sol(total+a[pos],pos+1)
    
for t in range(int(input())):
    global n,k,a
    c=0
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    sol(0,0)
    print(f'#{t+1}',c)